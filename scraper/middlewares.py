# https://doc.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals
from .exceptions import *


class ScraperSpiderMiddleware(object):
  # Not all methods need to be defined. If a method is not defined,
  # scrapy acts as if the spider middleware does not modify the
  # passed objects.

  @classmethod
  def from_crawler(cls, crawler):
      # This method is used by Scrapy to create your spiders.
      s = cls()
      crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
      return s

  def process_start_requests(self, start_requests, spider):
      # Called with the start requests of the spider, and works
      # similarly to the process_spider_output() method, except
      # that it doesn’t have a response associated.

      # Must return only requests (not items).
      for csv_read in start_requests:
        url = 'https://twitter.com/{}/status/{}'.format(
            csv_read.uid, csv_read.tid)
        request = spider.make_requests_from_url(url)
        request._meta = dict(csv_read=csv_read)
        yield request

  def process_spider_input(self, response, spider):
      # Called for each response that goes through the spider
      # middleware and into the spider.

      # Should return None or raise an exception.
      if response.url.endswith('suspended'):
        raise ScrapeException.SUSPENDED(response.url)
      return None

  def process_spider_output(self, response, result, spider):
      # Called with the results returned from the Spider, after
      # it has processed the response.

      # Must return an iterable of Request, dict or Item objects.
      yield from result

  def process_spider_exception(self, response, exception, spider):
      # Called when a spider or process_spider_input() method
      # (from other spider middleware) raises an exception.

      # Should return either None or an iterable of Response, dict
      # or Item objects.
      if exception and response.status == 200:
        raise ScrapeException.WRAP(response.url, exception)
      return []

  def spider_opened(self, spider):
      spider.logger.info('Spider opened: %s' % spider.name)

