# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class User(scrapy.Item):
  id = scrapy.Field()
  handle = scrapy.Field()
  name = scrapy.Field()


class Tweet(scrapy.Item):
  id = scrapy.Field()
  user = scrapy.Field()
  created_at = scrapy.Field()
  body = scrapy.Field()
  atreplies = scrapy.Field()
  links = scrapy.Field()

