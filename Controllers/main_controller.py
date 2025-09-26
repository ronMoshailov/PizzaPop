from Controllers.menu_controller import MenuController
from Controllers.top_frame_controller import TopFrameController
from Models.users_model import Users
from Views.data_window_view import DataWindowView
from Views.menu_view import MenuView
from Views.order_entry_view import OrderEntryView
from Views.top_frame_view import TopFrameView


class MainController:
    def __init__(self, root):
        # --- data --- #
        self.root = root

        # --- models --- #
        self.users_model = Users()

        # --- views --- #
        self.menu_view = MenuView(self.root)
        self.data_window_view = DataWindowView(self.root)
        self.top_frame_view = TopFrameView(self.root)
        self.order_entry_view = OrderEntryView(self.root)

        # --- controllers --- #
        self.menu_controller = MenuController(self.menu_view, self.data_window_view, self.users_model, self.display_user)
        self.top_frame_controller = TopFrameController(self.top_frame_view)

    # --- methods --- #
    def start_app(self):
        """
        This method start the main window.
        :return:
        """
        self.menu_controller.show_menu()
        self.top_frame_controller.show_top_frame()

    def display_user(self, text):
        user = self.users_model.is_user_exist(text)
        if user is None:
            print("user not found")

