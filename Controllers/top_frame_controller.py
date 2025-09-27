class TopFrameController:
    def __init__(self, top_frame_view):
        self.top_frame_view = top_frame_view

    def show_top_frame(self):
        self.top_frame_view.create_top_frame()

    def update_top_frame(self, full_name, phone_number, address):
        self.top_frame_view.update(full_name, phone_number, address)

    def clear_user(self):
        self.top_frame_view.clear()
