import unittest


class SampleTest(unittest.TestCase):

  def test_sample(self):
    foo = 1
    self.assertEqual(foo, 1)
