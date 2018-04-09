import os

SEED=42

class Path:
  DATA_DIR = 'data'
  MODEL_DIR = 'models'
  TWEETS_RAW_TEXT = None
  TWEETS_SN_PARSED_JSON = None
  TWEETS_CRAWLED_JSON = None

  @staticmethod
  def data(fname: str) -> str:
    return os.path.join(Path.DATA_DIR, fname)

  @staticmethod
  def model(fname: str) -> str:
    return os.path.join(Path.MODEL_DIR, fname)

Path.TWEETS_RAW_TEXT=Path.data('tweets_normalized.txt')
Path.TWEETS_SN_PARSED_JSON=Path.data('parsed_start_0.json')
Path.TWEETS_CRAWLED_JSON=Path.data('tweets.json')

