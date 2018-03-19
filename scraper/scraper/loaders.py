import dateutil.parser
import scrapy.loader.processors as proc
import dateutil.parser

from scrapy.loader import ItemLoader
from unicodedata import normalize
from .items import *
from .exceptions import *


def add_selector(loader_self, name_str, selector_str):
  selector = loader_self.selector.css(selector_str)
  loader_self.add_value(name_str, selector)
ItemLoader.add_selector = add_selector


def only(list_):
  if len(list_) > 1:
    raise ScrapeException.LOADER(
        'Expected only 1 element in {} but got {}'.format(
            list_, len(list_)))
  return list_[0]


def to_date(str_):
  # '2:09 AM - 25 Mar 2016' => '2:09 AM , 25 Mar 2016'
  return dateutil.parser.parse(str_.replace('-', ','))


def gettext(el):
  return ''.join([normalize('NFKD', e.root) for e in el.css('::text')])


class BodyItemLoader(ItemLoader):
  default_input_processor = proc.MapCompose(gettext)
  default_output_processor = proc.Join('')

  # lists
  atreplies_out = proc.Identity()
  links_out = proc.Identity()


class UserItemLoader(ItemLoader):
  default_output_processor = proc.Join('')


def extract_tweet_meta(div_wrap):
   tweet_xpath = div_wrap.xpath("@data-tweet-id")
   user_xpath = div_wrap.xpath("@data-user-id")

   return Parent(
       tweet_id=only(tweet_xpath.extract()),
       user_id=only(user_xpath.extract())) \
     if len(tweet_xpath) and len(user_xpath) else None


class _TweetLoader(ItemLoader):

  CSS_BASE_FORMAT = '.'.join(
      'div tweet permalink-tweet js-actionable-user js-actionable-tweet '
      'js-original-tweet[data-tweet-id={}]'.split())

  # CSS_BASE = '.'.join(
  #     'div tweet permalink-tweet js-actionable-user js-actionable-tweet '
  #     'js-original-tweet'.split())

  CSS_BASE = 'div[role="main"] div.permalink-inner'

  default_input_processor = proc.MapCompose(gettext)
  default_output_processor = proc.Join('')

  created_at_in = proc.TakeFirst()
  created_at_out = proc.Compose(only, to_date)

  user_in = proc.Identity()
  user_out = proc.Compose(only)

  body_in = proc.Identity()
  body_out = proc.Compose(only)

  parent_in = proc.Compose(extract_tweet_meta)
  parent_out = proc.TakeFirst()

  retweet_count_in = \
  favorite_count_in = \
  reply_count_in = proc.TakeFirst()

  label_in = proc.Identity()
  label_out = proc.TakeFirst()

  user = None
  body = None
  stats = None

  def load_item(self):
    self.add_value('user', self.user.load_item())
    self.add_value('body', self.body.load_item())
    return super().load_item()


class TweetLoader:
  def __new__(cls, response):
    # it's not always true that
    # csv_read(uid, tid) == user_id, tweet_id
    # due to the fact that we have csv_read as the source of truth,
    # we will store that into the metadata.
    csv_read = response.meta.get('csv_read')
    user_handle, tweet_id = response.url.split('/')[-2:]
    item = Tweet(id=csv_read.tid)

    # css_str = _TweetLoader.CSS_BASE_FORMAT.format(csv_read.tid)
    base_selector = response.css(_TweetLoader.CSS_BASE)

    obj = _TweetLoader(item, base_selector, response)
    obj.csv_read = csv_read

    tweet_selector = '*[data-tweet-id="{}"]'.format(tweet_id)
    obj.tweet_selector = base_selector.css(tweet_selector)
    obj.stat_selector = lambda name: obj.tweet_selector.css(
        '.ProfileTweet-action--{} span::attr(data-tweet-stat-count)'
          .format(name)).extract()

    obj.body = BodyItemLoader(
        Body(), obj.tweet_selector.css('.js-tweet-text-container'))
    obj.user = UserItemLoader(
        User(id=csv_read.uid), obj.tweet_selector.css('.permalink-header'))

    if any(len(s) == 0 for s in (obj.body.selector, obj.user.selector)):
      raise ScrapeException.SELECTOR(
          "Did not find any items with CSS {} for {}".format(
              base_selector, response.url))

    obj.add_value('label', csv_read.label)
    return obj

