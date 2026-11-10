import unittest
from label import LABEL
class ExactLabel(unittest.TestCase):
    def test_label_exact(self):
        self.assertEqual(LABEL, "Order reference")
