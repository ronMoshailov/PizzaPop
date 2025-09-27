import tkinter as tk

class TopFrameView:
    def __init__(self, root):
        self.root = root
        self.phone_label = None
        self.name_label = None

    def create_top_frame(self):
        top_frame = tk.Frame(self.root, bg="#640300", height=60)  # אדום כהה תואם למנובר
        top_frame.pack(side="top", fill="x", pady=(0,0), padx=0)

        # --- phone_label --- #
        self.phone_label = tk.Label(
            top_frame,
            text="050-1234567",
            font=("Arial", 22, "bold"),
            bg="#460006",  # צבע רקע הכפתור
            fg="white",  # צבע טקסט
            bd=0,
            padx=20,
            pady=10,
            relief="flat",
            highlightthickness=3,
            highlightbackground="#C04000",  # קו גבול כהה אדום
        )
        self.phone_label.pack(side="left", padx=12, pady=10)

        # --- name_label --- #
        self.name_label = tk.Label(
            top_frame,
            text="יוסי כהן",
            font=("Arial", 22, "bold"),
            bg="#460006",  # צבע רקע הכפתור
            fg="white",  # צבע טקסט
            bd=0,
            padx=20,
            pady=10,
            relief="flat",
            highlightthickness=3,
            highlightbackground="#c28413",  # קו גבול חום
        )
        self.name_label.pack(side="right", padx=12, pady=10)

    def update(self, full_name, phone_number):
        self.phone_label.config(text=phone_number)
        self.name_label.config(text=full_name)

    def clear(self):
        self.phone_label.config(text="מספר פלאפון")
        self.name_label.config(text="שם לקוח")
