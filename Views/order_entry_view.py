import tkinter as tk
from tkinter import messagebox, ttk


class OrderEntryView:
    def __init__(self, root, add_order_method, get_user_method):
        self.root = root
        self.add_order_method = add_order_method
        self.get_user_method = get_user_method

    def show_window(self):
        self.window = tk.Toplevel()
        self.window.title("הזנת הזמנה חדשה")
        self.window.configure(bg="#7a1c1c")  # בורדו חמים כמו רוטב עגבניות

        self.products = {}

        # --- style --- #
        label_style = {
            "font": ("Arial", 16, "bold"),
            "bg": "#7a1c1c",
            "fg": "white",
            "pady": 5
        }

        entry_style = {
            "font": ("Arial", 14),
            "bd": 2,
            "relief": "solid"
        }

        # --- content --- #
        form_frame = tk.Frame(self.window, bg="#7a1c1c")
        form_frame.pack(fill="both", padx=20, pady=10)

        form_frame.columnconfigure(0, weight=1) # weight -> label = 0, entry/button = 1
        form_frame.columnconfigure(1, weight=0) # weight -> label = 0, entry/button = 1

        # --- phone number --- #
        self.phone_label = tk.Label(form_frame, text=":מספר פלאפון של הלקוח", **label_style, anchor="e")
        self.phone_label.grid(row=0, column=1, sticky="e", padx=(0, 10), pady=5)

        self.phone_entry = tk.Entry(form_frame, **entry_style)
        self.phone_entry.grid(row=0, column=0, sticky="we", pady=5, ipady=4)

        # --- check user button --- #
        self.check_user_button = tk.Button(
            form_frame,
            text="בדוק",
            font=("Arial", 16, "bold"),
            bg="#221de2",
            fg="white",
            relief="raised",
            padx=15,
            pady=5,
            command=lambda: self.get_user_method(self.phone_entry.get().strip(), self.window)
        )
        self.check_user_button.grid(row=1, column=1, sticky="e", pady=5)

        # --- name --- #
        self.name_label = tk.Label(form_frame, text=":שם הלקוח", **label_style, anchor="e")
        self.name_label.grid(row=2, column=1, sticky="e", padx=(0, 10), pady=5)

        self.name_entry = tk.Entry(form_frame, **entry_style)
        self.name_entry.grid(row=2, column=0, sticky="we", pady=5, ipady=4)

        # --- address --- #
        self.address_label = tk.Label(form_frame, text=":כתובת", **label_style, anchor="e")
        self.address_label.grid(row=3, column=1, sticky="e", padx=(0, 10), pady=5)

        self.address_entry = tk.Entry(form_frame, **entry_style)
        self.address_entry.grid(row=3, column=0, sticky="we", pady=5, ipady=4)

        # --- separator --- #
        separator = ttk.Separator(form_frame, orient="horizontal")
        separator.grid(row=4, column=0, columnspan=2, sticky="we", pady=10)

        # --- product name --- #
        self.product_name_label = tk.Label(form_frame, text=":שם מוצר", **label_style, anchor="e")
        self.product_name_label.grid(row=5, column=1, sticky="e", padx=(0, 10), pady=5)

        self.product_name_entry = tk.Entry(form_frame, **entry_style)
        self.product_name_entry.grid(row=5, column=0, sticky="we", pady=5, ipady=4)

        # --- quantity --- #
        self.quantity_label = tk.Label(form_frame, text=":כמות", **label_style, anchor="e")
        self.quantity_label.grid(row=6, column=1, sticky="e", padx=(0, 10), pady=5)

        self.quantity_entry = tk.Entry(form_frame, **entry_style)
        self.quantity_entry.grid(row=6, column=0, sticky="we", pady=5, ipady=4)

        # --- add product button --- #
        self.add_product_button = tk.Button(
            form_frame,
            text="➕ הוסף מוצר",
            font=("Arial", 16, "bold"),
            bg="#e63946",
            fg="white",
            relief="raised",
            padx=15,
            pady=5,
            command=self.add_product
        )
        self.add_product_button.grid(row=7, column=1, sticky="e", pady=10)

        # --- products list box --- #
        self.products_listbox = tk.Listbox(
            form_frame,
            width=40,
            height=8,
            font=("Arial", 14),
            bg="#fff7e6",
            fg="#333",
            bd=2,
            relief="solid"
        )
        self.products_listbox.grid(row=8, column=0, columnspan=2, sticky="we", pady=10)

        # --- submit button --- #
        self.submit_button = tk.Button(
            form_frame,
            text="✅ סיום ושלח",
            font=("Arial", 18, "bold"),
            bg="#2a9d8f",
            fg="white",
            relief="raised",
            padx=20,
            pady=10,
            command=lambda: self.add_order_method(
                self.phone_entry.get().strip(),
                self.name_entry.get().strip(),
                self.address_entry.get().strip(),
                self.products,
                self.window
            )
        )
        self.submit_button.grid(row=9, column=0, columnspan=2, pady=15)

    def add_product(self):
        name = self.product_name_entry.get().strip()
        quantity = self.quantity_entry.get().strip()

        if not name or not quantity:
            messagebox.showerror("שגיאה", "יש למלא שם מוצר וכמות.", parent=self.window)
            return

        if not quantity.isdigit() or not int(quantity) >= 1:
            messagebox.showerror("שגיאה", "הכמות צריכה להיות רק מספר שלם חיובי.", parent=self.window)
            return

        self.products[name] = quantity
        self.products_listbox.insert(tk.END, f"{name} - {quantity}")
        self.product_name_entry.delete(0, tk.END)
        self.quantity_entry.delete(0, tk.END)

    def update(self, name, address):
        self.name_entry.delete(0, tk.END)
        self.name_entry.insert(0, name)

        self.address_entry.delete(0, tk.END)
        self.address_entry.insert(0, address)
