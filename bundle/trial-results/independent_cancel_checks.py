import unittest,sys,importlib.util,copy
from pathlib import Path
root=Path(sys.argv.pop(1)).resolve()
def load(name,p):
 spec=importlib.util.spec_from_file_location(name,p);m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m);return m
Stockroom=load('subject',root/'stockroom.py').Stockroom
class Acceptance(unittest.TestCase):
 def test_ac1_detached_lowercase_result(self):
  s=Stockroom(5);i=s.hold('a','u',2);r=s.cancel('a','u',i);self.assertEqual(r,s.orders[i]);self.assertEqual(r['state'],'cancelled');self.assertIsNot(r,s.orders[i]);r['quantity']=999;self.assertEqual(s.orders[i]['quantity'],2)
 def test_ac2_exact_stock_restoration(self):
  for q in (1,2,5):
   with self.subTest(quantity=q):
    s=Stockroom(5);i=s.hold('a','u',q);s.cancel('a','u',i);self.assertEqual(s.available,5)
 def test_ac3_repeated_result_without_release(self):
  s=Stockroom(5);i=s.hold('a','u',2);first=s.cancel('a','u',i)
  for _ in range(4):
   again=s.cancel('a','u',i);self.assertEqual(again,first);self.assertIsNot(again,first);self.assertIsNot(again,s.orders[i]);self.assertEqual(s.available,5)
 def test_ac4_ac5_identity_before_state_and_no_mutation(self):
  for state in ('held','cancelled','collected'):
   for tenant,owner in [('b','u'),('a','v'),('b','v')]:
    with self.subTest(state=state,tenant=tenant,owner=owner):
     s=Stockroom(5);i=s.hold('a','u',2)
     if state=='cancelled':s.cancel('a','u',i)
     if state=='collected':s.collect('a','u',i)
     before=copy.deepcopy(s.__dict__)
     with self.assertRaises(PermissionError):s.cancel(tenant,owner,i)
     self.assertEqual(s.__dict__,before)
 def test_ac6_collected_rejected_unchanged(self):
  s=Stockroom(5);i=s.hold('a','u',2);s.collect('a','u',i);before=copy.deepcopy(s.__dict__)
  with self.assertRaises(ValueError):s.cancel('a','u',i)
  self.assertEqual(s.__dict__,before);self.assertEqual(s.available,3)
 def test_ac7_missing_unchanged(self):
  s=Stockroom();before=copy.deepcopy(s.__dict__)
  with self.assertRaises(PermissionError):s.cancel('a','u',999)
  self.assertEqual(s.__dict__,before)
 def test_preserve_cancel_then_collect(self):
  s=Stockroom(5);i=s.hold('a','u',2);s.cancel('a','u',i);before=copy.deepcopy(s.__dict__)
  with self.assertRaises(ValueError):s.collect('a','u',i)
  self.assertEqual(s.__dict__,before)
 def test_indirect_future_hold_and_mixed_conservation(self):
  s=Stockroom(9);a=s.hold('a','u',3);b=s.hold('b','v',4);s.collect('b','v',b);s.cancel('a','u',a);c=s.hold('a','u',5)
  self.assertEqual(s.available,0);self.assertEqual(s.view('b','v',b)['state'],'collected');s.cancel('a','u',a);self.assertEqual(s.available,0);s.cancel('a','u',c);self.assertEqual(s.available,5)
  self.assertEqual(s.available+sum(o['quantity'] for o in s.orders.values() if o['state']=='held'),9-sum(o['quantity'] for o in s.orders.values() if o['state']=='collected'))
 def test_preserve_existing_copy_and_invalid_hold(self):
  s=Stockroom(5);i=s.hold('a','u',1);r=s.view('a','u',i);r['state']='bad';self.assertEqual(s.view('a','u',i)['state'],'held')
  for qty in (0,-1,True,1.5,6):
   before=copy.deepcopy(s.__dict__)
   with self.assertRaises(ValueError):s.hold('a','u',qty)
   self.assertEqual(s.__dict__,before)
unittest.main(verbosity=2)
