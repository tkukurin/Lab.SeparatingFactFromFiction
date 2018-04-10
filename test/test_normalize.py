import unittest

from syntaxnet.data_process import normalize


class TestNormalize(unittest.TestCase):

  def test_newline(self):
    x = 'this is a\nnewline tweet'
    self.assertEqualIterable(
        normalize([x]), 'this is a newline tweet')

  def test_url(self):
    x = 'a website called pic.twitter.com/url test'
    self.assertEqualIterable(
        normalize([x]), 'a website called @url test')

  def test_username_dotcom(self):
    x = 'US wary of lease of port in Australia; Marine base could be target of ' \
        'spying @nytimes.com'
    self.assertEqualIterable(
        normalize([x]), 'us wary of lease of port in australia; '
                        'marine base could be target of spying @user')

  def test_url_http(self):
    url = 'http://cultura.elpais.com/cultura/2016/03/22/actualidad' \
          '/1458642987_028773.html?id_externo_rsoc=TW_CC'
    x = 'a website called {} test'.format(url)
    self.assertEqualIterable(
        normalize([x]), 'a website called @url test')

  def test_url_nospace(self):
    url = 'http://www.vox.com/2016/3/25/11304336/justin-trudeau-canada-feminism' \
          '-fatherhood?utm_campaign=vox&utm_content=feature%3Atop&utm_medium=' \
          'social&utm_source=twitter'
    x = 'a website called{} test'.format(url)
    self.assertEqualIterable(
        normalize([x]), 'a website called @url test')

  def test_url_ampersand_percent_hashtag_underscore_comma_plus_colon(self):
    url = 'http://www.vox.com/2016/3/24/11296168/down-with-diet-books?utm_campaign' \
          '=vox&utm_content=feature%3A#fixed&utm_medium=social&utm_source' \
          '=twitter+test:test2,,comma'
    x = 'a website called {} test'.format(url)
    self.assertEqualIterable(
        normalize([x]), 'a website called @url test')

  def test_url_nospace_https(self):
    url = 'https://google.co.uk/123/abc/xyz?key=value&k2=v2'
    x = 'a website called{} test'.format(url)
    self.assertEqualIterable(
        normalize([x]), 'a website called @url test')

  def test_url_no_www(self):
    url = 'google.co.uk/123/abc/xyz?key=value&k2=v2#test'
    x = 'a website called {} test'.format(url)
    self.assertEqualIterable(
        normalize([x]), 'a website called @url test')

  def test_link_username_hashtag(self):
    x = 'Starbucks will start donating 100% of its unused food to those in need ' \
        'http://mashable.com/2016/03/22/starbucks-food-donations-foodshare/' \
        '#WQ2TeNi9q059 ... via @mashable  #welldoneStarbucks'
    self.assertEqualIterable(
        normalize([x]), 'starbucks will start donating 100% of its unused '
                        'food to those in need @url ... via @user  '
                        '@hashtag')

  def test_no_url(self):
    x = 'confessed to trying...'
    self.assertEqualIterable(
        normalize([x]), 'confessed to trying...')

  def test_hashtag_in_sequence(self):
    x = 'my #first #second #third these are all #hashtags'
    self.assertEqualIterable(
        normalize([x]), 'my @hashtag  @hashtag  @hashtag these are all '
                        '@hashtag')

  def test_hashtag_from_text(self):
    x = '@AJEnglish @marwanbishara It only proved that #Syria is another ' \
        '#Libya #Iraq. For long, #war is fought far on foreign soil.'
    self.assertEqualIterable(
        normalize([x]), '@user @user it only proved that @hashtag is another'
                        '@hashtag @hashtag. for long, @hashtag is fought far'
                        'on foreign soil.')


  def assertEqualIterable(self, got, expect):
    self.assertEqual(next(got), expect)
