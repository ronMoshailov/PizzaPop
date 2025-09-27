from Models.product_model import Product


class Order:
    def __init__(self):
        self.products = []

    def add_product(self, name, quantity):
            for product in self.products:
                if product.name == name:
                    print("product already exist in DB.")
                    return
            self.products.append(Product(name, quantity))
