import re
import pandas as pd
from util import compose, const


# replace with @[a-zA-Z] since this is username format for Twitter
regex_key_value = [
  # mail
  ('@email', r'([a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+)'),
  # @reply
  # people usually use @user.com for e.g. @nytimes.com
  ('@user', '(@[A-Za-z0-9\_]+(?:.com)?)'),
  # URL; just guess abc.xyz is a URL. don't capture inner groups.
  ('@url',
  '('
  '(?:(?:https?:\/\/|www\.)\S*)'
  '|'
  '(?:[d\w]+\.)+(?:[a-z]{2,6}(?:\.[a-z]{,6})?\S*)'
  ')'),
  # hashtag
  # https://stackoverflow.com/questions/8451846/actual-twitter-format-for-hashtags-not-your-regex-not-his-code-the-actual
  # punctuation terminates hashtag, must be preceeded by space
  ('@hashtag', '(#[A-Za-z0-9\_]+)'),
]
keys = [k for k, v in regex_key_value]
values = [v for k, v in regex_key_value] + [
  # punctuation will be tagged by SyntaxNet,
  # remove newline for easier input
  '\\n',
  '\\r',
]
regex_str = '|'.join('\\s*{}\\s*'.format(i) for i in values)

def regex_normalize(match):
  for match_group, replacement in enumerate(keys, start=1):
    if match.group(match_group):
      return ' {} '.format(replacement)
  return ' '


def remove_crap(tweet_content):
  return re.sub(regex_str, regex_normalize, tweet_content)


from sklearn.pipeline import TransformerMixin
class TweetNormalizer(TransformerMixin):

  def __init__(self):
    self.pipeline = compose(
      str.lower, remove_crap, str.strip)
    self.fit = lambda *x: self

  def transform(self, x):
    return self.pipeline(x)


def normalize(tweets):
  normalizer = TweetNormalizer()
  return map(normalizer.transform, tweets)


if __name__ == '__main__':
  import sys
  if len(sys.argv) != 2:
    raise Exception('Use: program.py [multi|binary]')
  type_ = sys.argv[1]
  tweets = pd.read_json(
    const.FileManager.TWEETS_CRAWLED_JSON if type_[0] == 'm' else \
    const.FileManager.TWEETS_MULTICLASS_CRAWLED_JSON if type_[0] == 'b' else \
    None)
  content = tweets['body'].apply(lambda dict_: dict_['content'])
  with open(const.Path.data('tweets-normalized-%s.txt' % type_[0]), 'w') as f:
    for tweet in normalize(content):
      print(tweet, file=f)

