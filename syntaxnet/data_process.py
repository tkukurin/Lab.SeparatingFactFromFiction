import re
import os
import pandas as pd
from util import compose

DATA = '../data'
TWEET_FILE = os.path.join(DATA, 'tweets.json')


def regex_normalize(match):
  AT, URL, HASHTAG = 1, 2, 3
  if match.group(AT):
    return ' @user '
  if match.group(URL):
    return ' @url '
  if match.group(HASHTAG):
    return ' @hashtag '
  return ' '


def remove_crap(tweet_content):
  regex = '|'.join([
    # @reply
    '(@[A-Za-z0-9_]+)',
    # URL (just guess abc.xyz is URL). don't capture inner groups.
    '((?:http[s]?://)?(?:www\.)?\S+\.[a-z]{2,6}/?\S*)',
    # hashtag
    '(#\S+)',
    # punctuation will be tagged by SyntaxNet, probably can extract from there.
    # '(\.,-:;)',
  ])
  return re.sub(regex, regex_normalize, tweet_content)


def normalize(tweets):
  pipeline = compose(
      str.lower,
      remove_crap,
      str.strip)

  return map(pipeline, tweets)


if __name__ == '__main__':
  tweets = pd.read_json(TWEET_FILE)
  content = tweets['body'].apply(lambda dict_: dict_['content'])
  with open(os.path.join(DATA, 'tweets_normalized.txt'), 'w') as f:
    for tweet in normalize(content):
      print(tweet, file=f)

