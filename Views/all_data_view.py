import tkinter as tk

class AllDataView:
    def __init__(self, root):
        self.root = root

    def show_window(self, users_model):
            window = tk.Toplevel(self.root)
            window.title("Users Data")
            text = tk.Text(window)
            text.pack(fill="both", expand=True)

            for user in users_model.users:
                text.insert("end", f"------------------------------------------------------------\n")
                text.insert("end", f"------------ name: {user.full_name}\n")
                text.insert("end", f"------------ phone: {user.phone_number}\n")
                text.insert("end", f"------------ address: {user.address}\n")
                for idx, order in enumerate(user.orders):
                    text.insert("end", f"-------- order #{idx + 1} \n")
                    text.insert("end", f"-------- time #{order.time} \n")
                    for product in order.products:
                        text.insert("end", f"---- product: {product.name:<15}, qty: {product.quantity:<15}\n")
                    text.insert("end", "\n")
