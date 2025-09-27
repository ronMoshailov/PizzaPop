from Models.product_model import Product
from Models.order_model import Order


class User:
    def __init__(self, full_name, phone_number):
        self.full_name = full_name
        self.phone_number = phone_number
        self.orders = []

    def add_order(self, order):
        new_order = Order()
        for product, quantity in order:
            new_order.add_product(product, quantity)
        self.orders.append(new_order)

# def add_product(self, name, quantity):
    #     for product in self.products:
    #         if product.name == name:
    #             print("product already exist in DB.")
    #             return
    #     self.products.append(Product(name, quantity))

    # def remove_product(self, name, quantity):
    #     for product in self.products:
    #         if product.name == name:
    #             self.products.remove(product)
    #             return
    #     print("Product doesn't exist in DB.")
