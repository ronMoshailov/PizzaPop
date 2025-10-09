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
