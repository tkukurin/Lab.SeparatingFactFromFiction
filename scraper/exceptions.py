class SuspendedException(Exception):
  def __init__(self, url):
    super().__init__(url)



class ScrapeException(Exception):
  SELECTOR = lambda s: Exception("[SELECTOR] {}".format(s))
  SUSPENDED = SuspendedException
  WRAP = lambda url, e: Exception("[WRAPPED url={}] {}".format(url, str(e)))
  LOADER = lambda s: Exception("[LOADER] {}".format(s))