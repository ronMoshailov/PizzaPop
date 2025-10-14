from Models.product_model import Product
from Models.order_model import Order


class User:
    def __init__(self, full_name, phone_number, address):
        self.full_name = full_name
        self.phone_number = phone_number
        self.address = address
        self.orders = []

    def add_order(self, order):
        new_order = Order()
        for product, quantity in order:
            new_order.add_product(product, quantity)
        self.orders.append(new_order)

    def to_dict(self):
        return {
            "full_name": self.full_name,
            "phone_number": self.phone_number,
            "address": self.address,
            "orders": [o.to_dict() for o in self.orders]
        }

    @staticmethod
    def from_dict(data):
        user = User(data["full_name"], data["phone_number"])
        user.address = data.get("address", "")
        for o in data.get("orders", []):
            user.orders.append(Order.from_dict(o))
        return user
