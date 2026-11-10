class Stockroom:
    def __init__(self, available=10):
        self.available = available
        self.orders = {}

    def hold(self, tenant, owner, quantity):
        if not isinstance(quantity, int) or isinstance(quantity, bool) or quantity <= 0 or quantity > self.available:
            raise ValueError("invalid quantity")
        oid = len(self.orders) + 1
        self.orders[oid] = dict(tenant=tenant, owner=owner, quantity=quantity, state="held")
        self.available -= quantity
        return oid

    def view(self, tenant, owner, oid):
        order = self.orders.get(oid)
        if order is None or order["tenant"] != tenant or order["owner"] != owner:
            raise PermissionError("not accessible")
        return dict(order)

    def collect(self, tenant, owner, oid):
        order = self.view(tenant, owner, oid)
        if order["state"] != "held":
            raise ValueError("not held")
        self.orders[oid]["state"] = "collected"
        return self.view(tenant, owner, oid)

    def cancel(self, tenant, owner, oid):
        order = self.view(tenant, owner, oid)
        if order["state"] == "cancelled":
            return self.view(tenant, owner, oid)
        if order["state"] != "held":
            raise ValueError("not held")
        self.orders[oid]["state"] = "cancelled"
        self.available += self.orders[oid]["quantity"]
        return self.view(tenant, owner, oid)
