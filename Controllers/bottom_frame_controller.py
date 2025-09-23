from Views.bottom_frame_view import BottomFrameView


class BottomFrameController:
    def __init__(self, model):
        self.model = model
        self.view = BottomFrameView()

    def show_orders(self, root, orders):
        self.view.create_bottom_frame(root, orders)
