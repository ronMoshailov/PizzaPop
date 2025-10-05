from Models.product_model import Product
from Models.order_model import Order


class User:
    def __init__(self, full_name, phone_number):
        self.full_name = full_name
        self.phone_number = phone_number
        self.address = "בן גוריון 870/13"
        self.orders = []

    def add_order(self, order):
        new_order = Order()
        for product, quantity in order:
            new_order.add_product(product, quantity)
        self.orders.append(new_order)

