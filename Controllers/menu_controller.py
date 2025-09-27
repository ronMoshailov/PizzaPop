import tkinter as tk


class MenuController:
    def __init__(self, menu_view, all_data_view, order_entry_view, users_model, display_user_method, clear_user_method):
        self.menu_view = menu_view
        self.all_data_view = all_data_view
        self.order_entry_view = order_entry_view
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
        # יוצרים חלון חדש
        window = tk.Toplevel(self.menu_view.root)
        window.title("בדיקת לקוח")
        window.geometry("300x150")

        # תווית
        label = tk.Label(window, text="שם לקוח או מספר פלאפון:")
        label.pack(pady=10)

        # תיבת טקסט
        entry = tk.Entry(window)
        entry.pack(pady=5)

        button = tk.Button(window, text="בדוק", command=lambda : self.display_user_method(entry.get(), window))
        button.pack(pady=10)

    def display_order_entry_view(self):
        self.order_entry_view.show_window()