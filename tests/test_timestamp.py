import unittest
from boddle import boddle
from blackapi import gettimestamp


class TestStatus(unittest.TestCase):
    def testRoot(self):
        with boddle():
            self.assertIn('{"timestamp":', gettimestamp())
