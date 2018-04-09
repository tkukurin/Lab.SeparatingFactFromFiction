import re
import pandas as pd
from util import compose, const


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
  # also remove surrounding whitespace
  regex = '|'.join('\\s*{}\\s*'.format(i) for i in [
    # @reply
    '(@[A-Za-z0-9_]+)',
    # URL (just guess abc.xyz is URL). don't capture inner groups.
    '((https?:\/\/)?([\da-z\.-]+)\.([a-z\.]{2,6})([\/\w\?\=\&\.-]*)*\/?\S)',
    # hashtag
    '(#\S+)',
    # punctuation will be tagged by SyntaxNet,
    # remove newline for easier input
    '\\n',
    '\\r',
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
  tweets = pd.read_json(const.Path.TWEETS_CRAWLED_JSON)
  content = tweets['body'].apply(lambda dict_: dict_['content'])
  with open(const.Path.data('tweets-normalized-v2.txt'), 'w') as f:
    for tweet in normalize(content):
      print(tweet, file=f)

