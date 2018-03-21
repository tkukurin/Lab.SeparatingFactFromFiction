import re
import os
import functools
import pandas as pd

DATA = '../data'
TWEET_FILE = os.path.join(DATA, 'tweets.json')


def compose(*fs):
  return lambda value: \
    functools.reduce(lambda f, v: f(v), fs, value)


def remove_crap(tweet_content):
  atreplies = r'(@[A-Za-z0-9_]+)'
  urls = r'http:\S+'
  not_word = r'([^0-9A-Za-z \t])'

  regex = '|'.join(v for k, v in locals() if k != 'tweet_content')
  return re.sub(regex, '', tweet_content)


def to_utf8(unicode_):
  return unicode_.encode('utf-8')


def normalize(tweets):
  pipeline = compose(
      to_utf8,
      str.lower,
      remove_crap,
      str.strip)

  return map(pipeline, tweets)


if __name__ == '__main__':
  tweets = pd.read_json(TWEET_FILE)
  content = tweets['body']['content']

