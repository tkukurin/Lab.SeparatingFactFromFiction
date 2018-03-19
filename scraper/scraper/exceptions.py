
class ScrapeException(Exception):
  SELECTOR = lambda s: Exception("[SELECTOR] {}".format(s))
  SUSPENDED = lambda url: Exception("[SUSPENDED] Account {}", url)
  WRAP = lambda url, e: Exception("[WRAPPED url={}] {}".format(url, str(e)))
  LOADER = lambda s: Exception("[LOADER] {}".format(s))