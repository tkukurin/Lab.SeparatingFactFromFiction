import joblib
import pathlib
import os
import logging as log


SEED: int = 42
binary_metrics: list = ['roc_auc', 'accuracy', 'average_precision']
multiclass_metrics: list = ['f1_micro', 'f1_macro']


def _find_dir_containing(fname):
  cur = os.path.abspath(os.curdir)
  while not os.path.exists(os.path.join(cur, fname)):
    if os.path.dirname(cur) == cur:
      raise Exception('{}: cannot find data dir {}'.format(__file__, fname))
    cur = os.path.dirname(cur)
  return cur


ROOT_DIR = _find_dir_containing('.git')
DATA_DIR = os.path.join(ROOT_DIR, 'data')
MODEL_DIR = os.path.join(ROOT_DIR, 'models')

log.info('Using {} as root directory'.format(ROOT_DIR))
for f in (DATA_DIR, ROOT_DIR, MODEL_DIR):
  if not os.path.exists(f):
    log.warning('Expected {}, but was not found'.format(f))


class FileManager:
  TWEETS_RAW_TEXT = None
  TWEETS_SN_PARSED_JSON = None
  TWEETS_CRAWLED_JSON = None

  def __init__(self, prefix=''):
    self.data_dir = DATA_DIR
    self.root_dir = ROOT_DIR
    self.model_dir = MODEL_DIR
    self.prefix = prefix

  def data(self, fname: str) -> pathlib.Path:
    return pathlib.Path(self.data_dir, self.prefix + fname)

  def model(self, fname: str) -> pathlib.Path:
    return pathlib.Path(self.model_dir, self.prefix + fname)
  
  def root(self, fname: str) -> pathlib.Path:
    return pathlib.Path(self.root_dir, self.prefix + fname)

  def save_model(self, obj: object, fname: str, overwrite=False):
    path = self.model(fname)

    if not overwrite and path.exists():
      raise Exception('Path {} exists'.format(path))

    with path.open('wb') as f:
      joblib.dump(obj, f)

  def load_model(self, obj: object, fname: str):
    with self.model(fname).open('rb') as f:
      return joblib.load(obj, f)


FileManager.TWEETS_RAW_TEXT = FileManager().data('tweets_normalized.txt')
FileManager.TWEETS_SN_PARSED_JSON = FileManager().data('tweets_sn_parsed.json')
FileManager.TWEETS_CRAWLED_JSON = FileManager().data('tweets.json')
FileManager.TWEETS_MULTICLASS_CRAWLED_JSON = FileManager().data('multiclass_tweets.json')


class Path:
  TWEETS_RAW_TEXT = None
  TWEETS_SN_PARSED_JSON = None
  TWEETS_CRAWLED_JSON = None

  @staticmethod
  def data(fname: str) -> str:
    return os.path.join(DATA_DIR, fname)

  @staticmethod
  def model(fname: str) -> str:
    return os.path.join(MODEL_DIR, fname)

