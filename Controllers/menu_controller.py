class MenuController:
    def __init__(self, view):
        self.view = view
        self.top_bar_dict = {
            "ראשי": [("יציאה", self.close_app)],
            "הזמנות": [("הוספת הזמנה", self.print_data)],
            "הגדרות": [("הראה כמות שורות", None), ("אופציה 3.2", None)],
            "נקה": None,
        }

    def show_menu(self, root):
        # שולח ל־View את הנתונים ואת ה-root כדי להציג
        self.view.create_menu(root, self.top_bar_dict)

    def print_data(self):
        for user in self.users:
            print(f"שם: {user.full_name}")
            print(f"פלאפון: {user.phone_number}")
            for product in user.products:
                product.print()
            print("")

    def close_app(self):
        print("exit")