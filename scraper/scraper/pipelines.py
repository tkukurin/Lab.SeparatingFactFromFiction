# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import scrapy.loader.processors as proc
import dateutil.parser

from scrapy.loader import ItemLoader
from .items import User, Tweet


class TweetToJson(object):

  def process_item(self, item, spider):
    return item
