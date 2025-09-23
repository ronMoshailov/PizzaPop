import tkinter as tk
from tkinter import ttk

from Variables import orders, top_bar_dict

# --- create frames --- #
def create_menu_bar(root):
    top_bar = tk.Frame(root, bg="#222222", height=50)  # רקע כהה
    top_bar.pack(side="top", fill="x")

    for title, options in top_bar_dict.items():
        menu_button = tk.Menubutton(
            top_bar,
            text=title,
            bg="#460006",        # צבע רקע הכפתור
            fg="white",          # צבע טקסט
            activebackground="#555555",  # רקע בעת ריחוף
            activeforeground="white",    # טקסט בעת ריחוף
            font=("Arial", 14, "bold"),
            relief="raised",
            bd=2,
            padx=10,
            pady=5
        )
        menu = tk.Menu(menu_button, tearoff=0, bg="white", fg="black", font=("Arial", 12))
        for option in options:
            menu.add_command(label=option)
        menu_button.config(menu=menu)
        menu_button.pack(side="right", padx=5, pady=5)

def create_top_frame(frame_root):
    # --- top_frame --- #
    top_frame = tk.Frame(frame_root, bg="#640300", height=60)  # אדום כהה תואם למנובר
    top_frame.pack(side="top", fill="x", pady=(0,0), padx=0)

    # --- phone_label --- #
    phone_label = tk.Label(
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
    phone_label.pack(side="left", padx=12, pady=10)

    # --- name_label --- #
    name_label = tk.Label(
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
    name_label.pack(side="right", padx=12, pady=10)

def create_bottom_frame(root):
    # --- create bottom frame --- #
    bottom_frame = ttk.Frame(root)
    bottom_frame.pack(side="top", fill="both", expand=True)

    # --- create canvas frame --- #
    canvas = tk.Canvas(bottom_frame, bg="#fc031a")  # create canvas

    # --- create scrollbar --- #
    scrollbar_x = ttk.Scrollbar(bottom_frame, orient="horizontal", command=canvas.xview)  # create scrollbar
    scrollbar_x.pack(side="bottom", fill="x")  # set the scrollbar in the bottom

    # --- create frame --- #
    scrollable_frame = tk.Frame(canvas, bg="#fc031a")  # create scrollable frame
    scrollable_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))  # run function when scrollable changes

    # --- add orders to window --- #
    for order_id, items in orders.items():
        frame = create_order_frame(scrollable_frame, order_id, items)
        frame.pack(side="right", padx=(40,0))

    # --- connect canvas --- #
    canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")  # add widget to window
    canvas.configure(xscrollcommand=scrollbar_x.set)  # connect scrollbar to canvas

    # --- set canvas --- #
    canvas.pack(side="top", fill="both", expand=True)

    # --- set canvas --- #
    scrollable_frame.update_idletasks()  # עדכון scrollregion אחרי שכל ההזמנות נוספו
    canvas.xview_moveto(1)  # תצוגה מתחילה מימין

# --- general --- #
def create_order_frame(parent, order_id, items):
    frame = ttk.Frame(parent, padding=10)
    frame.configure(style="OrderFrame.TFrame")

    # --- Label הזמנה --- #
    label = tk.Label(
        frame,
        text=f"#{order_id} הזמנה",
        font=("Comic Sans MS", 28, "bold"),
        bg="#F4A261",  # כתום חם
        fg="#6D2E00",  # חום כהה
        padx=10,
        pady=5,
        relief="ridge",
        bd=2
    )
    label.pack(side="top", fill="x", pady=(0,10))

    # --- style לעץ --- #
    style = ttk.Style()
    style.configure("Custom.Treeview", font=("Arial", 18), rowheight=30, background="#FFE5B4", foreground="#6D2E00")
    style.configure("Custom.Treeview.Heading", font=("Arial", 20, "bold"), background="#ffc386", foreground="#7c3f00")

    # --- מסגרת ל-Treeview + Scrollbar --- #
    table_frame = tk.Frame(frame, bg="#FFE5B4", bd=2, relief="groove")
    table_frame.pack(side="top", fill="both", expand=True)

    table = ttk.Treeview(table_frame, columns=("qty", "name"), show="headings", height=24, style="Custom.Treeview")

    table.heading("qty", text="כמות", anchor="center")
    table.heading("name", text="שם", anchor="center")

    table.column("qty", width=100, anchor="center")
    table.column("name", width=400, anchor="e")

    # --- Scrollbar אנכי --- #
    scrollbar = ttk.Scrollbar(table_frame, orient="vertical", command=table.yview)
    table.configure(yscrollcommand=scrollbar.set)

    table.pack(side="right", fill="both", expand=True, padx=(0,0))
    scrollbar.pack(side="right", fill="y")

    # --- הוספת מוצרים --- #
    for item_name, qty in items:
        table.insert("", "end", values=(qty, item_name))

    return frame


def option_selected(option):
    print("נבחרה אופציה:", option)

def create_menu_option(menubar, title, options):
    menu = tk.Menu(menubar, tearoff=0)
    for option in options:
        menu.add_command(label=option, command=lambda: option_selected(option))
    menubar.add_cascade(label=title, menu=menu)

