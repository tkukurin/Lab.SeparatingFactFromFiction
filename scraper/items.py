# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class RelatedTweet(scrapy.Item):
  tweet_id = scrapy.Field()
  user_id = scrapy.Field()
  date = scrapy.Field()


class User(scrapy.Item):
  id = scrapy.Field()
  handle = scrapy.Field()
  name = scrapy.Field()
  is_verified = scrapy.Field()


class Body(scrapy.Item):
  content = scrapy.Field()
  atreplies = scrapy.Field()
  links = scrapy.Field()
  hashtags = scrapy.Field()


class Media(scrapy.Item):
  url = scrapy.Field()
  title = scrapy.Field()
  content = scrapy.Field()
  content_source = scrapy.Field()
  data_source = scrapy.Field()


class Tweet(scrapy.Item):
  created_at = scrapy.Field()
  id = scrapy.Field()

  parents = scrapy.Field()
  children = scrapy.Field()
  user = scrapy.Field()
  body = scrapy.Field()
  media = scrapy.Field()

  retweet_count = scrapy.Field()
  favorite_count = scrapy.Field()
  reply_count = scrapy.Field()

  label = scrapy.Field()




