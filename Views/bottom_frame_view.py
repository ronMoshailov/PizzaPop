import tkinter as tk
from tkinter import ttk


class BottomFrameView:
    def __init__(self):
        pass

    def create_order_frame(self, parent, order_id, items):
        frame = ttk.Frame(parent, padding=10)
        frame.configure(style="OrderFrame.TFrame")

        # כותרת
        label = tk.Label(
            frame,
            text=f"#{order_id} הזמנה",
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
        for item_name, qty in items:
            table.insert("", "end", values=(qty, item_name))

        return frame

    def create_bottom_frame(self, root, orders):
        bottom_frame = ttk.Frame(root)
        bottom_frame.pack(side="top", fill="both", expand=True)

        canvas = tk.Canvas(bottom_frame, bg="#fc031a")

        scrollbar_x = ttk.Scrollbar(bottom_frame, orient="horizontal", command=canvas.xview)
        scrollbar_x.pack(side="bottom", fill="x")

        scrollable_frame = tk.Frame(canvas, bg="#fc031a")
        scrollable_frame.bind("<Configure>", lambda e: canvas.configure(
            scrollregion=canvas.bbox("all")))

        # הוספת הזמנות
        for order_id, items in orders.items():
            frame = self.create_order_frame(scrollable_frame, order_id, items)
            frame.pack(side="right", padx=(40, 0))

        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(xscrollcommand=scrollbar_x.set)

        canvas.pack(side="top", fill="both", expand=True)

        scrollable_frame.update_idletasks()
        canvas.xview_moveto(1)