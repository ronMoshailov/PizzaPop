class User:
    def __init__(self, full_name, phone_number):
        self.full_name = full_name
        self.phone_number = phone_number
        self.orders = []
        