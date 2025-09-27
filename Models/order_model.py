from Models.product_model import Product


class Order:
    def __init__(self, time="00:00"):
        self.products = []
        self.time = time

    def add_product(self, name, quantity):
            for product in self.products:
                if product.name == name:
                    print("product already exist in DB.")
                    return
            self.products.append(Product(name, quantity))
