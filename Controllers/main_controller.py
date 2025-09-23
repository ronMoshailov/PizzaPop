from Controllers.bottom_frame_controller import BottomFrameController
from Controllers.menu_controller import MenuController
from Controllers.top_frame_controller import TopFrameController
from Models.users import Users
from Views.bottom_frame_view import BottomFrameView
from Views.menu_view import MenuView
from Views.top_frame_view import TopFrameView


class MainController:
    def __init__(self, root):
        # --- data --- #
        self.root = root

        users_model = Users()

        # --- views --- #
        self.menu_view = MenuView()
        # self.top_frame_view = TopFrameView()
        self.bottom_frame_view = BottomFrameView(users_model)

        # --- controllers --- #
        self.menu_controller = MenuController(self.menu_view)
        # self.top_frame_controller = TopFrameController(self.top_frame_view)
        self.bottom_frame_controller = BottomFrameController(self.bottom_frame_view)

        self.menu_controller.show_menu(self.root)


