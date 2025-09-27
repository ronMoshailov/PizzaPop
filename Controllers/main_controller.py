from tkinter import messagebox

from Controllers.menu_controller import MenuController
from Controllers.top_frame_controller import TopFrameController
from Models.order_model import Order
from Models.users_model import Users
from Views.all_data_view import AllDataView
from Views.menu_view import MenuView
from Views.order_entry_view import OrderEntryView
from Views.orders_view import OrdersView
from Views.top_frame_view import TopFrameView


class MainController:
    def __init__(self, root):
        # --- data --- #
        self.root = root

        # --- models --- #
        self.users_model = Users()

        # --- views --- #
        self.menu_view = MenuView(self.root)
        self.all_data_view = AllDataView(self.root)
        self.top_frame_view = TopFrameView(self.root)
        self.orders_view = OrdersView(self.root)
        self.order_entry_view = OrderEntryView(self.root, self.add_order)

        # --- controllers --- #
        self.menu_controller = MenuController(self.menu_view, self.all_data_view, self.order_entry_view, self.users_model, self.display_user, self.clear_user)
        self.top_frame_controller = TopFrameController(self.top_frame_view)

    # --- methods --- #
    def start_app(self):
        """
        This method start the main window.
        :return:
        """
        self.menu_controller.show_menu()
        self.top_frame_controller.show_top_frame()

    def display_user(self, text, window):
        user = self.users_model.is_user_exist(text)
        if user is None:
            messagebox.showerror("שגיאה", "מספר הפלאפון לא נמצא")
            return
        self.top_frame_controller.update_top_frame(user.full_name, user.phone_number)
        self.orders_view.create(user)
        window.destroy()

    def clear_user(self):
        self.top_frame_controller.clear_user()

    def add_order(self, phone_number, product_dict, window):
        user = self.users_model.is_user_exist(phone_number)
        if user is None:
            messagebox.showerror("שגיאה", "מספר הפלאפון לא נמצא")
            return
        new_order = Order()
        for name, quantity in product_dict.items():
            new_order.add_product(name, quantity)
        user.orders.append(new_order)
        messagebox.showinfo("הודעה", "ההזמנה נוספה בהצלחה")
        window.destroy()
