import unittest
from label import LABEL
class Existing(unittest.TestCase):
    def test_label_exists(self):
        self.assertIsInstance(LABEL,str)
        self.assertTrue(LABEL)
