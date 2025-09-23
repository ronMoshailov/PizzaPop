from Models.product import Product


class User:
    def __init__(self, full_name, phone_number):
        self.full_name = full_name
        self.phone_number = phone_number
        self.products = []

    def add_product(self, name, quantity):
        for product in self.products:
            if product.name == name:
                print("product already exist in DB.")
                return
        self.products.append(Product(name, quantity))

    # def remove_product(self, name, quantity):
    #     for product in self.products:
    #         if product.name == name:
    #             self.products.remove(product)
    #             return
    #     print("Product doesn't exist in DB.")
