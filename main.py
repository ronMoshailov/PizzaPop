import tkinter as tk

from functions import create_top_frame, create_bottom_frame, create_menu_bar

# --- root --- #
root = tk.Tk()
root.title("PizzaPop")
root.state("zoomed")
root.configure(bg="green")

# --- menu bar --- #
create_menu_bar(root)

# --- top frame --- #
create_top_frame(root)

# --- bottom frame --- #
create_bottom_frame(root)

# --- active loop --- #
root.mainloop()
