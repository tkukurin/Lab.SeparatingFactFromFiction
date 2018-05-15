import logging as log
import pandas as pd
from .const import FileManager

def dict_get(key):
  if isinstance(key, str):
    return lambda i: i[key]
  return lambda i: [v for k, v in i.items() if k in key]


as_list = lambda v: v if isinstance(v, list) else [v]
def dict_filter(key):
  return lambda i: dict(
      filter(lambda kv: kv[0] in as_list(key), i.items()))


# dictionary keys become df columns for given existing columns
def expand_to_columns(df, key):
  key = [key] if isinstance(key, str) else key
  expanded = [df[k].apply(pd.Series) for k in key]
  for k, e in zip(key, expanded):
    e.columns = ['{}_{}'.format(k, c) for c in e.columns]
  return pd.concat([df.drop(key, axis=1)] + expanded, axis=1)


def stream_lines(fname):
  with open(fname) as f:
    yield from map(lambda s: s.strip(), f)

from . import compose
read_lines = compose(stream_lines, list)


def load_df(clean=True) -> pd.DataFrame:
  # df = pd.read_json(FileManager.TWEETS_SN_PARSED_JSON).dropna()
  df_original = pd.read_json(FileManager.TWEETS_CRAWLED_JSON)
  df_expanded = expand_to_columns(df_original, ['user', 'body'])
  # ret = df.join(df_expanded, on='index').drop_duplicates(['input'])
  ret = df_expanded
  log.info("Loaded DF with keys", ret.keys())
  return cleanup_df(ret) if clean else ret

def load_df_multi(clean=True) -> pd.DataFrame:
  df_original = pd.read_json(FileManager.TWEETS_MULTI_CRAWLED_JSON)
  df_expanded = expand_to_columns(df_original, ['user', 'body'])
  ret = df_expanded
  log.info("Loaded DF with keys", ret.keys())
  return cleanup_df(ret) if clean else ret
  

def cleanup_df(df):
  return df.drop_duplicates(subset='body_content')


out_word = dict_get('word')
out_pos = dict_get('pos_tag')
