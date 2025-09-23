from Models.user import User


class Users:
    def __init__(self):
        self.users = []

    def add_user(self, full_name, phone_number):
        for user in self.users:
            if user.full_name == full_name and user.phone_number == phone_number:
                print("User already exists in DB.")
                return user
        new_user = User(full_name, phone_number)
        self.users.append(new_user)
        return new_user
