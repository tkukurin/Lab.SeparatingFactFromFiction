import scrapy
import csv

from collections import namedtuple
from ..loaders import TweetLoader


CsvRead = namedtuple('CsvRead', ['uid', 'tid', 'label'])
def load_csv(location):
  with open(location, 'r') as f:
    reader = csv.reader(f)
    headers = next(reader)

    uid = headers.index('user_id')
    tid = headers.index('tweet_id')
    label = headers.index('label')

    for row in filter(lambda r: len(r), reader):
      yield CsvRead(row[uid], row[tid], row[label])


class TwitterSpider(scrapy.Spider):
  name = 'twitter'
  domain = 'https://twitter.com'

  def __init__(self, location=None, **kwargs):
    super().__init__(**kwargs)
    self.location = location

  def start_requests(self):
    return load_csv(self.location)

  def parse(self, response):
    loader = TweetLoader(response=response)

    loader.add_css('created_at', '.tweet-details-fixer .metadata span::text')
    loader.add_selector('parents', '.ancestor.tweet')
    loader.add_selector('children', '.descendant.tweet')

    loader.add_value('retweet_count', loader.stat_selector('retweet'))
    loader.add_value('reply_count', loader.stat_selector('reply'))
    loader.add_value('favorite_count', loader.stat_selector('favorite'))

    loader.user.add_css('name', 'a strong.fullname::text')
    loader.user.add_css('handle', 'a span.username b::text')
    loader.user.add_value(
        'is_verified', len(loader.user.selector.css('.Icon--verified')) > 0)

    loader.body.add_selector('content', 'p')
    loader.body.add_selector('atreplies', '.twitter-atreply')
    loader.body.add_selector('links', '.twitter-timeline-link .js-display-url')
    loader.body.add_selector('hashtags', '.twitter-hashtag')

    iframe_url = loader.tweet_selector.css(
        '.js-media-container div::attr(data-src)').extract()
    if iframe_url:
      yield scrapy.Request(
          self.domain + iframe_url[0],
          loader.parse_iframe)
    else:
      yield loader.load_item()

