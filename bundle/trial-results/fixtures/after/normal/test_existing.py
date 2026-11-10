import unittest
from stockroom import Stockroom

class ExistingBehaviour(unittest.TestCase):
    def test_hold_reduces_stock(self):
        s=Stockroom(5);i=s.hold("a","u",2);self.assertEqual(s.available,3);self.assertEqual(s.view("a","u",i)["state"],"held")
    def test_cross_tenant_denied(self):
        s=Stockroom();i=s.hold("a","u",1)
        with self.assertRaises(PermissionError):s.view("b","u",i)
    def test_cross_owner_denied(self):
        s=Stockroom();i=s.hold("a","u",1)
        with self.assertRaises(PermissionError):s.view("a","v",i)
    def test_collection(self):
        s=Stockroom(5);i=s.hold("a","u",2);self.assertEqual(s.collect("a","u",i)["state"],"collected");self.assertEqual(s.available,3)
    def test_invalid_quantities(self):
        for q in (0,-1,True,11):
            with self.assertRaises(ValueError):Stockroom().hold("a","u",q)
    def test_view_is_copy(self):
        s=Stockroom();i=s.hold("a","u",1);s.view("a","u",i)["state"]="changed";self.assertEqual(s.view("a","u",i)["state"],"held")

if __name__ == "__main__": unittest.main()
