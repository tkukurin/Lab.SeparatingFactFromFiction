# -*- coding: utf-8 -*-
import scrapy
import csv
import dateutil.parser
import scrapy.loader.processors as proc
import dateutil.parser
import unicodedata

from scrapy.loader import ItemLoader
from ..items import Tweet, User
from collections import namedtuple
import json


CsvRead = namedtuple('CsvRead', ['uid', 'tid'])
def load_csv(location):
  with open(location, 'r') as f:
    reader = csv.reader(f)
    headers = next(reader)
    uid = headers.index('user_id')
    tid = headers.index('tweet_id')

    for row in reader:
      yield CsvRead(row[uid], row[tid])


def only(list_):
  if len(list_) > 1:
    raise Exception(
        'Expected only 1 element in {} but got {}'.format(
            list_, len(list_)))
  return list_[0]


def to_date(str_):
  # '2:09 AM - 25 Mar 2016' => '2:09 AM , 25 Mar 2016'
  return dateutil.parser.parse(str_.replace('-', ','))


def gettext(el):
  # if isinstance(el, str):
  #   return el
  return ''.join(
      [unicodedata.normalize('NFKD', e.root) for e in el.css('::text')])


class TweetItemLoader(ItemLoader):
  default_input_processor = proc.MapCompose(gettext)
  default_output_processor = proc.Join('')

  created_at_in = proc.Identity()
  created_at_out = proc.Compose(only, to_date)

  user_in = proc.Identity()
  user_out = proc.Compose(only)

  # lists
  atreplies_out = proc.Compose(json.dumps)
  links_out = proc.Compose(json.dumps)


class UserItemLoader(ItemLoader):
  default_output_processor = proc.Join()


class TwitterSpider(scrapy.Spider):
  name = 'twitter'

  def __init__(self, location=None):
    self.location = location

  def start_requests(self):
    return load_csv(self.location)

  def parse(self, response):
    CSS_BASE = '.'.join(
        'div tweet permalink-tweet js-actionable-user js-actionable-tweet '
        'js-original-tweet'.split())
    csv_read = response.meta['csv_read']
    loader = TweetItemLoader(Tweet(id=csv_read.tid), response=response)\
        .nested_css(CSS_BASE)
    loader.add_css('created_at', '.tweet-details-fixer .metadata span::text')

    loader_head = UserItemLoader(
        User(id=csv_read.uid), loader.nested_css('.permalink-header').selector)
    loader_head.add_css('name', 'a strong.fullname::text')
    loader_head.add_css('handle', 'a span.username b::text')
    loader.add_value('user', loader_head.load_item())

    loader_body = loader.nested_css('.js-tweet-text-container')
    loader_body.add_value('body', loader_body.selector.css('p'))

    atreply = loader_body.selector.css('.twitter-atreply')
    loader_body.add_value('atreplies', atreply)

    links = loader_body.selector.css('.twitter-timeline-link .js-display-url')
    loader_body.add_value('links', links)

    yield loader.load_item()
