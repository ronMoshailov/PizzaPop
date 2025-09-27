import tkinter as tk
from tkinter import messagebox


class OrderEntryView:
    def __init__(self, root, add_order_method):
        self.root = root

        self.add_order_method = add_order_method

    def show_window(self):
        self.window = tk.Toplevel()
        self.window.title("הזנת הזמנה חדשה")

        self.products = {}

        self.phone_label = tk.Label(self.window, text="מספר פלאפון של הלקוח:")
        self.phone_label.pack(pady=5)

        self.phone_entry = tk.Entry(self.window)
        self.phone_entry.pack(pady=5)

        self.product_name_label = tk.Label(self.window, text="שם מוצר:")
        self.product_name_label.pack(pady=5)

        self.product_name_entry = tk.Entry(self.window)
        self.product_name_entry.pack(pady=5)

        self.quantity_label = tk.Label(self.window, text="כמות:")
        self.quantity_label.pack(pady=5)

        self.quantity_entry = tk.Entry(self.window)
        self.quantity_entry.pack(pady=5)

        self.add_product_button = tk.Button(self.window, text="הוסף מוצר", command=self.add_product)
        self.add_product_button.pack(pady=10)

        self.products_listbox = tk.Listbox(self.window, width=50)
        self.products_listbox.pack(pady=10)

        self.submit_button = tk.Button(self.window, text="סיום ושלח", command= lambda: self.add_order_method(self.phone_entry.get().strip(), self.products, self.window))
        self.submit_button.pack(pady=15)


    def add_product(self):
        name = self.product_name_entry.get().strip()
        quantity = self.quantity_entry.get().strip()

        if not name or not quantity:
            messagebox.showwarning("שגיאה", "יש למלא שם מוצר וכמות.")
            return

        # שמירה לרשימה
        self.products[name] = quantity

        # הצגה ב־Listbox
        self.products_listbox.insert(tk.END, f"{name} - {quantity}")

        # ניקוי שדות להזנה נוספת
        self.product_name_entry.delete(0, tk.END)
        self.quantity_entry.delete(0, tk.END)
