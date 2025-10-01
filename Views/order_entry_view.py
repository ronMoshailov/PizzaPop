import tkinter as tk
from tkinter import messagebox, ttk


class OrderEntryView:
    def __init__(self, root, add_order_method):
        self.root = root
        self.add_order_method = add_order_method

    def show_window(self):
        self.window = tk.Toplevel()
        self.window.title("הזנת הזמנה חדשה")
        self.window.configure(bg="#7a1c1c")  # בורדו חמים כמו רוטב עגבניות

        self.products = {}

        # --- טקסט + שדות --- #
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

        # פלאפון
        self.phone_label = tk.Label(self.window, text="מספר פלאפון של הלקוח:", **label_style)
        self.phone_label.pack(pady=(15, 5))

        self.phone_entry = tk.Entry(self.window, **entry_style)
        self.phone_entry.pack(pady=5, ipadx=10, ipady=5)

        # שם מוצר
        self.product_name_label = tk.Label(self.window, text="שם מוצר:", **label_style)
        self.product_name_label.pack(pady=5)

        self.product_name_entry = tk.Entry(self.window, **entry_style)
        self.product_name_entry.pack(pady=5, ipadx=10, ipady=5)

        # כמות
        self.quantity_label = tk.Label(self.window, text="כמות:", **label_style)
        self.quantity_label.pack(pady=5)

        self.quantity_entry = tk.Entry(self.window, **entry_style)
        self.quantity_entry.pack(pady=5, ipadx=10, ipady=5)

        # --- זמן אספקה --- #
        time_frame = tk.Frame(self.window, bg="#7a1c1c")
        time_frame.pack(pady=10)

        tk.Label(time_frame, text="שעה:", font=("Arial", 14, "bold"), bg="#7a1c1c", fg="white").grid(row=0, column=0, padx=5)
        self.hour_combo = ttk.Combobox(
            time_frame,
            values=[f"{i:02d}" for i in range(24)],
            width=5,
            state="readonly",
            font=("Arial", 12)
        )
        self.hour_combo.current(0)
        self.hour_combo.grid(row=0, column=1, padx=5)

        tk.Label(time_frame, text="דקות:", font=("Arial", 14, "bold"), bg="#7a1c1c", fg="white").grid(row=0, column=2, padx=5)
        self.minute_combo = ttk.Combobox(
            time_frame,
            values=[f"{i:02d}" for i in range(0, 60, 10)],
            width=5,
            state="readonly",
            font=("Arial", 12)
        )
        self.minute_combo.current(0)
        self.minute_combo.grid(row=0, column=3, padx=5)

        # --- כפתור הוספת מוצר --- #
        self.add_product_button = tk.Button(
            self.window,
            text="➕ הוסף מוצר",
            font=("Arial", 16, "bold"),
            bg="#e63946",
            fg="white",
            relief="raised",
            padx=15,
            pady=5,
            command=self.add_product
        )
        self.add_product_button.pack(pady=10)

        # --- רשימת מוצרים --- #
        self.products_listbox = tk.Listbox(
            self.window,
            width=40,
            height=8,
            font=("Arial", 14),
            bg="#fff7e6",
            fg="#333",
            bd=2,
            relief="solid"
        )
        self.products_listbox.pack(pady=10)

        # --- כפתור שליחה --- #
        self.submit_button = tk.Button(
            self.window,
            text="✅ סיום ושלח",
            font=("Arial", 18, "bold"),
            bg="#2a9d8f",
            fg="white",
            relief="raised",
            padx=20,
            pady=10,
            command=lambda: self.add_order_method(
                self.phone_entry.get().strip(),
                self.products,
                f"{self.hour_combo.get()}:{self.minute_combo.get()}",
                self.window
            )
        )
        self.submit_button.pack(pady=15)

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
