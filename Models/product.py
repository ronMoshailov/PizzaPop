class Product:
    def __init__(self, name, quantity):
        self.name = name
        self.quantity = quantity

    def print(self):
        print(f"שם: {self.name}")
        print(f"כמות: {self.quantity}")
