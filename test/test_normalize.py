from syntaxnet.data_process import normalize
import unittest

class TestNormalize(unittest.TestCase):

  def test_newline(self):
    x = 'this is a\nnewline tweet'
    self.assertEqualIterable(
        normalize([x]), 'this is a newline tweet')

  def test_url(self):
    x = 'a website called www.google.com test'
    self.assertEqualIterable(
        normalize([x]), 'a website called @url test')

  def test_url_https(self):
    x = 'a website called https://google.co.uk test'
    self.assertEqualIterable(
        normalize([x]), 'a website called @url test')

  def assertEqualIterable(self, got, expect):
    self.assertEqual(next(got), expect)
