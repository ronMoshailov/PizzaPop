import tkinter as tk
from tkinter import ttk


class UserEntryView:
    current_window = None

    def __init__(self, root):
        self.root = root

    def create_user_entry_frame(self, display_user_method):
        window = tk.Toplevel(self.root)
        window.title("בדיקת לקוח")
        window.geometry("400x150")
        window.configure(bg="#7a1c1c")  # רקע בורדו

        # --- מסגרת לשדות --- #
        frame = tk.Frame(window, bg="#7a1c1c")
        frame.pack(fill="both", expand=True, padx=20, pady=20)

        # הגדרת עמודות
        # הגדרת עמודות
        frame.columnconfigure(0, weight=1)  # Entry יתפשט לרוחב
        frame.columnconfigure(1, weight=0)  # Label לא יתפשט

        # --- Entry --- #
        entry = tk.Entry(
            frame,
            font=("Arial", 16),
            bd=2,
            relief="solid",
            justify="right"  # מימין לשמאל
        )
        entry.grid(row=0, column=0, sticky="we", ipady=4)
        entry.icursor(tk.END)  # הסמן מתחיל בצד ימין

        # --- Label --- #
        label = tk.Label(
            frame,
            text=":מספר פלאפון",
            font=("Arial", 18, "bold"),
            bg="#7a1c1c",
            fg="white",
            pady=5,
            anchor="e"
        )
        label.grid(row=0, column=1, sticky="e", padx=(10, 0))

        # --- Button --- #
        button = tk.Button(
            frame,
            text="בדוק",
            font=("Arial", 16, "bold"),
            bg="#2a9d8f",
            fg="white",
            relief="raised",
            padx=20,
            pady=8,
            command=lambda: display_user_method(entry.get(), window)
        )
        button.grid(row=1, column=0, columnspan=2, sticky="ew", pady=(10, 0))

