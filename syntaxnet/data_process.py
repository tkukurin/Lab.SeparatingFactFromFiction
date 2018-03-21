import re
import os
import functools
import pandas as pd

DATA = '../data'
TWEET_FILE = os.path.join(DATA, 'tweets.json')


def compose(*fs):
  return lambda value: \
    functools.reduce(lambda v, f: f(v), fs, value)


def remove_crap(tweet_content):
  atreplies = r'(@[A-Za-z0-9_]+)'
  urls = r'http:\S+'

  regex = '|'.join(
      v for k, v in locals().items()
      if k != 'tweet_content')
  return re.sub(regex, '', tweet_content)


def normalize(tweets):
  print(tweets)
  pipeline = compose(
      str.lower,
      remove_crap,
      str.strip)

  return map(pipeline, tweets)


if __name__ == '__main__':
  tweets = pd.read_json(TWEET_FILE)
  content = tweets['body'].apply(lambda dict_: dict_['content'])
  print(list(normalize(content[:1])))

