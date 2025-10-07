import tkinter as tk

from Controllers.main_controller import MainController

# --- root --- #
root = tk.Tk()
root.title("PizzaPop")
root.state("zoomed")
root.configure(bg="green")

# --- logo --- #
logo = tk.PhotoImage(file="Assets/logo.png")
root.iconphoto(True, logo)

# --- controllers --- #
main_controller = MainController(root)
main_controller.start_app()

# --- active loop --- #
root.mainloop()
