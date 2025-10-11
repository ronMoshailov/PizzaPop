class Product:
    def __init__(self, name, quantity):
        self.name = name
        self.quantity = quantity

    def print(self):
        print(f"שם: {self.name}")
        print(f"כמות: {self.quantity}")

    def to_dict(self):
        """
        for save data
        :return:
        """
        return {"name": self.name, "quantity": self.quantity}

    @staticmethod
    def from_dict(data):
        """
        for save data
        :return:
        """
        return Product(data["name"], data["quantity"])

