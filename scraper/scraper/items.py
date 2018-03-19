# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class Parent(scrapy.Item):
  tweet_id = scrapy.Field()
  user_id = scrapy.Field()


class User(scrapy.Item):
  id = scrapy.Field()
  handle = scrapy.Field()
  name = scrapy.Field()


class Body(scrapy.Item):
  content = scrapy.Field()
  atreplies = scrapy.Field()
  links = scrapy.Field()
  hashtags = scrapy.Field()


class Tweet(scrapy.Item):
  created_at = scrapy.Field()
  id = scrapy.Field()

  parents = scrapy.Field()
  children = scrapy.Field()
  user = scrapy.Field() #serializer=None)  # todo
  body = scrapy.Field()

  retweet_count = scrapy.Field()
  favorite_count = scrapy.Field()
  reply_count = scrapy.Field()

  label = scrapy.Field()




