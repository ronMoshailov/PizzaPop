import tkinter as tk
from tkinter import ttk


class UserEntryView:
    current_window = None

    def __init__(self, root):
        self.root = root

    def create_user_entry_frame(self, display_user_method):
        window = tk.Toplevel(self.root)
        window.title("בדיקת לקוח")
        window.geometry("380x220")
        window.configure(bg="#7a1c1c")  # רקע בורדו כמו רוטב עגבניות

        label = tk.Label(
            window,
            text="שם לקוח או מספר פלאפון:",
            font=("Arial", 18, "bold"),
            bg="#7a1c1c",
            fg="white",
            pady=10
        )
        label.pack(pady=(20, 10))

        # --- תיבת טקסט --- #
        entry = tk.Entry(
            window,
            font=("Arial", 16),
            bd=2,
            relief="solid",
            justify="center",
        )
        entry.insert(0, "0548348091")
        entry.pack(pady=5, ipadx=10, ipady=5)

        # --- כפתור בדיקה --- #
        button = tk.Button(
            window,
            text="בדוק",
            font=("Arial", 16, "bold"),
            bg="#2a9d8f",  # ירקרק נעים
            fg="white",
            relief="raised",
            padx=20,
            pady=8,
            command=lambda: display_user_method(entry.get(), window)
        )
        button.pack(pady=20)
    #
    # def create(self, user):
    #     if OrdersView.current_window is not None:
    #         try:
    #             OrdersView.current_window.destroy()
    #         except:
    #             pass
    #
    #     bottom_frame = ttk.Frame(self.root)
    #     OrdersView.current_window = bottom_frame
    #     bottom_frame.pack(side="top", fill="both", expand=True)
    #
    #     canvas = tk.Canvas(bottom_frame, bg="#fc031a")
    #
    #     scrollbar_x = ttk.Scrollbar(bottom_frame, orient="horizontal", command=canvas.xview)
    #     scrollbar_x.pack(side="bottom", fill="x")
    #
    #     scrollable_frame = tk.Frame(canvas, bg="#fc031a")
    #     scrollable_frame.bind("<Configure>", lambda e: canvas.configure(
    #         scrollregion=canvas.bbox("all")))
    #
    #     # הוספת הזמנות
    #     for idx, order in enumerate(user.orders):
    #         # for product in order.products:
    #         frame = self._create_order_frame(scrollable_frame, idx, order.products)
    #         frame.pack(side="left", padx=(40, 0))
    #
    #     canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
    #     canvas.configure(xscrollcommand=scrollbar_x.set)
    #
    #     canvas.pack(side="top", fill="both", expand=True)
    #
    #     scrollable_frame.update_idletasks()
    #     canvas.xview_moveto(1)
    #
    # def clear(self):
    #     if OrdersView.current_window is None:
    #         return
    #     OrdersView.current_window.destroy()
