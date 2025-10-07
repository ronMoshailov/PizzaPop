from Models.user_model import User


class Users:
    def __init__(self):
        self.users = []
        self._load_data()

    def add_user(self, full_name, phone_number):
        for user in self.users:
            if user.full_name == full_name and user.phone_number == phone_number:
                print("User already exists in DB.")
                return user
        new_user = User(full_name, phone_number)
        self.users.append(new_user)
        return new_user

    def is_user_exist(self, text):
        if not (text.isdigit() and len(text) == 10):
            return None
        for user in self.users:
            if user.phone_number == text:
                return user
        return None

    def _load_data(self):
        person_orders = {
            ("יוסי כהן", "0501234567"): [
                [
                    ("פיצה מרגריטה", 2),
                    ("קולה", 1),
                    ("לחם שום", 1),
                    ("רוטב שום", 2),
                    ("סלט אישי", 1)
                ]
            ],
            ("שרה לוי", "0522345678"): [
                [
                    ("פיצה משפחתית", 1),
                    ("מים", 2),
                    ("פיצה טבעונית", 1),
                    ("קולה זירו גדול", 2),
                    ("רוטב אלף האיים", 1)
                ]
            ],
            ("דוד ישראלי", "0533456789"): [
                [
                    ("פיצה בולגרית", 3),
                    ("סלט יווני", 1),
                    ("לחם שום", 2),
                    ("פיצה מרגריטה", 1),
                    ("רוטב שום", 2)
                ]
            ],
            ("מיכל כהן", "0544567890"): [
                [
                    ("פיצה מרגריטה", 2),
                    ("קולה", 2),
                    ("לחם שום", 1),
                    ("פיצה בולגרית", 1),
                    ("סלט אישי", 1)
                ]
            ],
            ("רון מושאילוב", "0548348091"): [
                [
                    ("פיצה משפחתית עם זיתים וטונה", 1),
                    ("קולה זירו גדול", 1),
                    ("פיצה טבעונית", 2),
                    ("רוטב אלף האיים", 2),
                    ("לחם שום", 1)
                ]
            ],
            ("רון מושאילוב", "0548348091"): [
                [
                    ("פיצה משפחתית עם זיתים וטונה", 1),
                    ("קולה זירו גדול", 1),
                    ("פיצה טבעונית", 2),
                    ("רוטב אלף האיים", 2),
                    ("לחם שום", 1)
                ],
                [
                    ("פיצה משפחתית עם זיתים קלמטה", 1),
                    ("קולה זירו גדול", 3)
                ],
                [
                    ("פיצה משפחתית עם אננס ואנשובי", 1),
                    ("קולה זירו גדול", 1),
                    ("פיצה משפחתית עם זיתים", 2),
                    ("רוטב אלף האיים", 2),
                ],
                [
                    ("פיצה משפחתית עם קורנפלקס וחביתה", 1),
                    ("קולה זירו גדול", 1),
                ],
                [
                    ("פיצה נפוליטנה", 1),
                    ("קולה זירו גדול", 1),
                ],
                [
                    ("פיצה משפחתית עם מילקי וכריות", 1),
                    ("קולה זירו גדול", 1),
                ]
            ]
        }
        for user_info, order_list in person_orders.items():
            full_name, phone_number = user_info
            new_user = self.add_user(full_name, phone_number)
            for order in order_list:
                new_user.add_order(order)
