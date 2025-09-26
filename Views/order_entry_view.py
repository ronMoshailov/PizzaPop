import tkinter as tk


class OrderEntryView:
    def __init__(self, root):
        self.root = root

    def show_window(self, users_model):
        self.products_buffer = []  # מאגר זמני של מוצרים

        self.frame = tk.Toplevel(self.root)
        # self.frame.pack(fill="x")

        # --- שדות לקוח --- #
        tk.Label(self.frame, text="שם לקוח:").grid(row=0, column=0, sticky="w")
        self.entry_name = tk.Entry(self.frame)
        self.entry_name.grid(row=0, column=1)

        tk.Label(self.frame, text="מספר פלאפון:").grid(row=1, column=0, sticky="w")
        self.entry_phone = tk.Entry(self.frame)
        self.entry_phone.grid(row=1, column=1)

        # --- שדות מוצר --- #
        tk.Label(self.frame, text="שם מוצר:").grid(row=2, column=0, sticky="w")
        self.entry_product = tk.Entry(self.frame)
        self.entry_product.grid(row=2, column=1)

        tk.Label(self.frame, text="כמות:").grid(row=3, column=0, sticky="w")
        self.entry_qty = tk.Entry(self.frame)
        self.entry_qty.grid(row=3, column=1)

        # --- כפתורים --- #
        self.btn_add_product = tk.Button(self.frame, text="הוסף מוצר")
        self.btn_add_product.grid(row=4, column=0, pady=5)

        self.btn_save_user = tk.Button(self.frame, text="שמור הזמנה")
        self.btn_save_user.grid(row=4, column=1, pady=5)

    def clear_product_fields(self):
        """מנקה את שדות המוצר"""
        self.entry_product.delete(0, tk.END)
        self.entry_qty.delete(0, tk.END)
