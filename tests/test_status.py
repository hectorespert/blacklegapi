import unittest
from boddle import boddle
from api import status


class TestStatus(unittest.TestCase):
    def testRoot(self):
        with boddle():
            self.assertEqual(status(), '{"status": true}')
