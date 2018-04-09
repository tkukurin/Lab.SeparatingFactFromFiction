import pandas as pd
from .const import Path

def load_df() -> pd.DataFrame:
  df = pd.read_json(Path.TWEETS_SN_PARSED_JSON).dropna()
  return df

def dict_get(key):
  if isinstance(key, str):
    return lambda i: i[key]
  return lambda i: [v for k, v in i.items() if k in key]

as_list = lambda v: v if isinstance(v, list) else [v]
def dict_filter(key):
  return lambda i: dict(
      filter(lambda kv: kv[0] in as_list(key), i.items()))

df_text = dict_get('input')
df_parse = dict_get('output')

out_word = dict_get('word')
out_pos = dict_get('pos_tag')
