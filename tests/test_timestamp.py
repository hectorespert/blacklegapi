import unittest

from boddle import boddle

from server.api import gettimestamp


class TestStatus(unittest.TestCase):
    def testRoot(self):
        with boddle():
            self.assertIn('{"timestamp":', gettimestamp())
