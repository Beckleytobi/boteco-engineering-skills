import unittest
from stockroom import Stockroom


class CancelBehaviour(unittest.TestCase):

    # AC-CANCEL-1: state is exact lowercase 'cancelled'; returned dict is a copy
    def test_cancel_state_and_copy(self):
        s = Stockroom(available=5)
        oid = s.hold("a", "u", 2)
        result = s.cancel("a", "u", oid)
        self.assertEqual(result["state"], "cancelled")
        result["state"] = "tampered"
        self.assertEqual(s.orders[oid]["state"], "cancelled")

    # AC-CANCEL-2: available fully restored after cancel
    def test_cancel_releases_stock(self):
        s = Stockroom(available=5)
        oid = s.hold("a", "u", 2)
        self.assertEqual(s.available, 3)
        s.cancel("a", "u", oid)
        self.assertEqual(s.available, 5)

    # AC-CANCEL-3: repeat cancel returns detached copy, no second release, no error
    def test_cancel_repeat_no_error(self):
        s = Stockroom(available=5)
        oid = s.hold("a", "u", 2)
        r1 = s.cancel("a", "u", oid)
        self.assertEqual(s.available, 5)
        r2 = s.cancel("a", "u", oid)
        self.assertEqual(s.available, 5)
        self.assertEqual(r1["state"], "cancelled")
        self.assertEqual(r2["state"], "cancelled")
        self.assertIsNot(r1, r2)

    # AC-CANCEL-4: wrong tenant raises PermissionError; stock and state unchanged
    def test_cancel_wrong_tenant(self):
        s = Stockroom()
        oid = s.hold("a", "u", 1)
        pre_available = s.available
        with self.assertRaises(PermissionError):
            s.cancel("b", "u", oid)
        self.assertEqual(s.available, pre_available)
        self.assertEqual(s.orders[oid]["state"], "held")

    # AC-CANCEL-5: wrong owner raises PermissionError; stock and state unchanged
    def test_cancel_wrong_owner(self):
        s = Stockroom()
        oid = s.hold("a", "u", 1)
        pre_available = s.available
        with self.assertRaises(PermissionError):
            s.cancel("a", "v", oid)
        self.assertEqual(s.available, pre_available)
        self.assertEqual(s.orders[oid]["state"], "held")

    # AC-CANCEL-6: cancel after collect raises ValueError; available remains 3 (not restored)
    def test_cancel_collected_raises(self):
        s = Stockroom(5)
        oid = s.hold("a", "u", 2)
        s.collect("a", "u", oid)
        self.assertEqual(s.available, 3)
        with self.assertRaises(ValueError):
            s.cancel("a", "u", oid)
        self.assertEqual(s.available, 3)
        self.assertEqual(s.orders[oid]["state"], "collected")

    # AC-CANCEL-7: missing oid raises PermissionError
    def test_cancel_missing_oid(self):
        s = Stockroom()
        with self.assertRaises(PermissionError):
            s.cancel("a", "u", 999)

    # INV-ISOLATION-1: wrong identity still denied even after the order is cancelled
    def test_cancel_wrong_identity_after_cancel(self):
        s = Stockroom()
        oid = s.hold("a", "u", 1)
        s.cancel("a", "u", oid)
        self.assertEqual(s.orders[oid]["state"], "cancelled")
        with self.assertRaises(PermissionError):
            s.cancel("b", "u", oid)
        with self.assertRaises(PermissionError):
            s.cancel("a", "v", oid)

    # AC-PRESERVE: collect after cancel raises ValueError (cancelled is terminal for collect)
    def test_collect_after_cancel_raises(self):
        s = Stockroom(5)
        oid = s.hold("a", "u", 2)
        s.cancel("a", "u", oid)
        with self.assertRaises(ValueError):
            s.collect("a", "u", oid)
        self.assertEqual(s.available, 5)
        self.assertEqual(s.orders[oid]["state"], "cancelled")

    # AC-PRESERVE: mutating the returned cancel dict does not alter stored order
    def test_returned_copy_no_mutation(self):
        s = Stockroom(5)
        oid = s.hold("a", "u", 2)
        copy = s.cancel("a", "u", oid)
        copy["state"] = "tampered"
        copy["quantity"] = 999
        self.assertEqual(s.orders[oid]["state"], "cancelled")
        self.assertEqual(s.orders[oid]["quantity"], 2)

    # AC-PRESERVE + INV-STOCK-1: stock restored by cancel enables a future hold
    def test_hold_after_cancel_restoration(self):
        s = Stockroom(available=5)
        oid = s.hold("a", "u", 5)
        self.assertEqual(s.available, 0)
        s.cancel("a", "u", oid)
        self.assertEqual(s.available, 5)
        oid2 = s.hold("a", "u", 3)
        self.assertEqual(s.available, 2)
        self.assertEqual(s.orders[oid2]["state"], "held")

    # INV-STOCK-1 + AC-LOCAL: inventory conservation through mixed hold/cancel/collect
    def test_inventory_conservation(self):
        initial = 10
        s = Stockroom(available=initial)
        oid1 = s.hold("a", "u", 3)
        oid2 = s.hold("a", "u", 2)
        oid3 = s.hold("b", "v", 4)
        s.collect("a", "u", oid1)
        s.cancel("a", "u", oid2)
        # oid3 still held
        held_qty = sum(
            o["quantity"] for o in s.orders.values() if o["state"] == "held"
        )
        collected_qty = sum(
            o["quantity"] for o in s.orders.values() if o["state"] == "collected"
        )
        self.assertEqual(s.available + held_qty + collected_qty, initial)

    # AC-CANCEL-4/5 + no-mutation: PermissionError leaves state and stock unchanged
    def test_no_mutation_on_permission_denial(self):
        s = Stockroom(5)
        oid = s.hold("a", "u", 2)
        pre = s.available
        with self.assertRaises(PermissionError):
            s.cancel("x", "u", oid)
        self.assertEqual(s.available, pre)
        self.assertEqual(s.orders[oid]["state"], "held")
        with self.assertRaises(PermissionError):
            s.cancel("a", "x", oid)
        self.assertEqual(s.available, pre)
        self.assertEqual(s.orders[oid]["state"], "held")

    # AC-CANCEL-6 + no-mutation: collected cancel denial leaves state and stock unchanged
    def test_no_mutation_on_collected_denial(self):
        s = Stockroom(5)
        oid = s.hold("a", "u", 2)
        s.collect("a", "u", oid)
        pre = s.available
        with self.assertRaises(ValueError):
            s.cancel("a", "u", oid)
        self.assertEqual(s.available, pre)
        self.assertEqual(s.orders[oid]["state"], "collected")


if __name__ == "__main__":
    unittest.main()
