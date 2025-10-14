from Models.product_model import Product


class Order:
    def __init__(self):
        self.products = []
        # self.time = time

    def add_product(self, name, quantity):
            for product in self.products:
                if product.name == name:
                    print("product already exist in DB.")
                    return
            self.products.append(Product(name, quantity))

    def to_dict(self):
        return {
            # "time": self.time,
            "products": [p.to_dict() for p in self.products]
        }

    @staticmethod
    def from_dict(data):
        order = Order()
        for p in data["products"]:
            order.products.append(Product.from_dict(p))
        return order