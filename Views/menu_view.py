import tkinter as tk

class MenuView:
    def __init__(self, root):
        self.root = root

    def create_menu(self, top_bar_dict):
        top_bar = tk.Frame(self.root, bg="#222222", height=50)  # רקע כהה
        top_bar.pack(side="top", fill="x")

        for title, tuple_options in top_bar_dict.items():
            # כפתור "נקה"
            if title == "נקה":
                clear_button = tk.Button(
                    top_bar,
                    text="נקה",
                    bg="#ea252b",  # צבע רקע
                    fg="white",  # צבע טקסט
                    activebackground="#8b0d11",
                    activeforeground="white",
                    font=("Arial", 12, "bold"),
                    bd=2,
                    padx=10,
                    pady=5,
                    command=lambda: tuple_options()  # פעולה של ה-CONTROLLER ניתן לחבר כאן
                )
                clear_button.pack(side="right", padx=5, pady=5)
                continue  # ממשיך לאופציות אחרות

            # כפתורי תפריט רגילים
            menu_button = tk.Menubutton(
                top_bar,
                text=title,
                bg="#460006",  # צבע רקע הכפתור
                fg="white",  # צבע טקסט
                activebackground="#ff0016",  # רקע בעת ריחוף
                activeforeground="white",  # טקסט בעת ריחוף
                font=("Arial", 14, "bold"),
                relief="raised",
                bd=2,
                padx=10,
                pady=5
            )
            menu = tk.Menu(menu_button, tearoff=0, bg="white", fg="black", font=("Arial", 12))
            for option, method in tuple_options or []:
                if method:
                    # חשוב להשתמש ב-lambda עם ברירת מחדל כדי לא לאבד את ההקשר
                    menu.add_command(label=option, command=lambda m=method: m())
            menu_button.config(menu=menu)
            menu_button.pack(side="right", padx=5, pady=5)

