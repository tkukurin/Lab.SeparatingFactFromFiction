import unittest

from syntaxnet.data_process import normalize


class TestNormalize(unittest.TestCase):

  def test_newline(self):
    x = 'this is a\nnewline tweet'
    self.assertEqualIterable(
        normalize([x]), 'this is a newline tweet')

  def test_url(self):
    x = 'a website calledwww.google.com test'
    self.assertEqualIterable(
        normalize([x]), 'a website called @url test')

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

  def test_url_nospace_https(self):
    url = 'https://google.co.uk/123/abc/xyz?key=value&k2=v2'
    x = 'a website called{} test'.format(url)
    self.assertEqualIterable(
        normalize([x]), 'a website called @url test')

  def assertEqualIterable(self, got, expect):
    self.assertEqual(next(got), expect)
