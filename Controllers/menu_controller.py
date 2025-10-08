import tkinter as tk


class MenuController:
    def __init__(self, menu_view, all_data_view, order_entry_view, user_entry_view, users_model, display_user_method, clear_user_method):
        self.menu_view = menu_view
        self.all_data_view = all_data_view
        self.order_entry_view = order_entry_view
        self.user_entry_view = user_entry_view
        self.users_model = users_model

        self.display_user_method = display_user_method
        self.clear_user_method = clear_user_method

    def show_menu(self):
        option_dict = {
            # "ראשי": [("יציאה", self.close_app)],
            "הזמנות": [("הוסף הזמנה", self.display_order_entry_view), ("הצג פרטים", None), ("צפה בהיסטוריה", self.print_data)],
            "מידע": [("הצג לקוח", self.display_user), ("אופציה 3.2", None)],
            "הגדרות": [("הראה כמות שורות", None), ("אופציה 3.2", None)],
            "נקה": self.clear_user_method,
        }
        self.menu_view.create_menu(option_dict)


    def print_data(self):
        self.all_data_view.show_window(self.users_model)


    def close_app(self):
        self.menu_view.root.destroy()

    def display_user(self):
        # --- כותרת --- #
        self.user_entry_view.create_user_entry_frame(self.display_user_method)

    def display_order_entry_view(self):
        self.order_entry_view.show_window()