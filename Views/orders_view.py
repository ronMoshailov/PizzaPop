import tkinter as tk
from tkinter import ttk


class OrdersView:
    current_window = None

    def __init__(self, root):
        self.root = root

    def _create_order_frame(self, scrollable_frame, idx, products):
        frame = ttk.Frame(scrollable_frame, padding=10)
        frame.configure(style="OrderFrame.TFrame")

        # כותרת
        label = tk.Label(
            frame,
            text=f"#{idx} הזמנה",
            font=("Comic Sans MS", 28, "bold"),
            bg="#F4A261",
            fg="#6D2E00",
            padx=10,
            pady=5,
            relief="ridge",
            bd=2
        )
        label.pack(side="top", fill="x", pady=(0, 10))

        # סגנון טבלה
        style = ttk.Style()
        style.configure("Custom.Treeview", font=("Arial", 18), rowheight=30,
                        background="#FFE5B4", foreground="#6D2E00")
        style.configure("Custom.Treeview.Heading", font=("Arial", 20, "bold"),
                        background="#ffc386", foreground="#7c3f00")

        # טבלה
        table_frame = tk.Frame(frame, bg="#FFE5B4", bd=2, relief="groove")
        table_frame.pack(side="top", fill="both", expand=True)

        table = ttk.Treeview(table_frame, columns=("qty", "name"),
                             show="headings", height=24,
                             style="Custom.Treeview")

        table.heading("qty", text="כמות", anchor="center")
        table.heading("name", text="שם", anchor="center")

        table.column("qty", width=100, anchor="center")
        table.column("name", width=400, anchor="e")

        scrollbar = ttk.Scrollbar(table_frame, orient="vertical", command=table.yview)
        table.configure(yscrollcommand=scrollbar.set)

        table.pack(side="right", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

        # הכנסת מוצרים
        for product in products:
            table.insert("", "end", values=(product.quantity, product.name))
        return frame

    def create(self, user):
        if OrdersView.current_window is not None:
            try:
                OrdersView.current_window.destroy()
            except:
                pass

        bottom_frame = ttk.Frame(self.root)
        OrdersView.current_window = bottom_frame
        bottom_frame.pack(side="top", fill="both", expand=True)

        canvas = tk.Canvas(bottom_frame, bg="#fc031a")

        scrollbar_x = ttk.Scrollbar(bottom_frame, orient="horizontal", command=canvas.xview)
        scrollbar_x.pack(side="bottom", fill="x")

        scrollable_frame = tk.Frame(canvas, bg="#fc031a")
        scrollable_frame.bind("<Configure>", lambda e: canvas.configure(
            scrollregion=canvas.bbox("all")))

        # הוספת הזמנות
        for idx, order in enumerate(user.orders):
            # for product in order.products:
            frame = self._create_order_frame(scrollable_frame, idx, order.products)
            frame.pack(side="right", padx=(40, 0))

        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(xscrollcommand=scrollbar_x.set)

        canvas.pack(side="top", fill="both", expand=True)

        scrollable_frame.update_idletasks()
        canvas.xview_moveto(1)

    def clear(self):
        if OrdersView.current_window is None:
            return
        OrdersView.current_window.destroy()
