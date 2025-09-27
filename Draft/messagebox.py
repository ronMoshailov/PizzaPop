import tkinter as tk
from tkinter import messagebox

def demo_messageboxes():
    root = tk.Tk()
    root.withdraw()  # מסתיר את חלון ה-root (נשארים רק ה-popups)

    # 1. הודעות מידע/אזהרה/שגיאה
    messagebox.showinfo("showinfo", "זהו showinfo — לחצו על אישור.")
    messagebox.showwarning("showwarning", "זהו showwarning — לחצו על אישור.")
    messagebox.showerror("showerror", "זהו showerror — לחצו על אישור.")

    # 2. שאלה שמחזירה 'yes' / 'no' (מחרוזת)
    ans = messagebox.askquestion("askquestion", "askquestion — האם אתם רואים זה?")
    print("askquestion returned:", ans)

    # 3. אישור/ביטול (True/False)
    ans = messagebox.askokcancel("askokcancel", "askokcancel — להמשיך?")
    print("askokcancel returned:", ans)

    # 4. כן/לא (Boolean)
    ans = messagebox.askyesno("askyesno", "askyesno — כן או לא?")
    print("askyesno returned:", ans)

    # 5. נסה שוב/ביטול (Boolean)
    ans = messagebox.askretrycancel("askretrycancel", "askretrycancel — לנסות שוב?")
    print("askretrycancel returned:", ans)

    # 6. כן/לא/בטל (מחזיר True / False / None)
    ans = messagebox.askyesnocancel("askyesnocancel", "askyesnocancel — כן/לא/בטל?")
    print("askyesnocancel returned:", ans)

    # סוף — להשמיד את ה-root
    root.destroy()

if __name__ == "__main__":
    demo_messageboxes()
