import re
import threading
from tkinter import messagebox
import tkinter as tk

from Controllers.menu_controller import MenuController
from Controllers.top_frame_controller import TopFrameController
from Models.order_model import Order
from Models.users_model import Users
from Views.all_data_view import AllDataView
from Views.menu_view import MenuView
from Views.order_entry_view import OrderEntryView
from Views.orders_view import OrdersView
from Views.top_frame_view import TopFrameView
from Views.user_entry_view import UserEntryView

from scapy.all import sniff

class MainController:
    def __init__(self, root):
        # --- data --- #
        self.root = root

        # --- models --- #
        self.users_model = Users()

        # --- views --- #
        self.menu_view = MenuView(self.root)
        self.all_data_view = AllDataView(self.root)
        self.top_frame_view = TopFrameView(self.root)
        self.orders_view = OrdersView(self.root)
        self.order_entry_view = OrderEntryView(self.root, self.add_order)
        self.user_entry_view = UserEntryView(self.root)

        # --- controllers --- #
        self.menu_controller = MenuController(self.menu_view, self.all_data_view, self.order_entry_view, self.user_entry_view, self.users_model, self.display_user, self.clear_user)
        self.top_frame_controller = TopFrameController(self.top_frame_view)

        # שמירה אוטומטית כשסוגרים את חלון ה-Tk
        self.root.protocol("WM_DELETE_WINDOW", self.on_close)

    def on_close(self):
        self._save_data()
        self.root.destroy()

    def _load_data(self):
        import json
        try:
            with open("data.json", "r", encoding="utf-8") as f:
                data = json.load(f)
            for u in data:
                user = self.users_model.add_user(u["full_name"], u["phone_number"])
                user.address = u.get("address", "")
                for order_list in u.get("orders", []):
                    order = Order()
                    for product in order_list:
                        order.add_product(product["name"], product["quantity"])
                    user.orders.append(order)
        except FileNotFoundError:
            pass  # הקובץ עוד לא קיים

    def _save_data(self):
        import json
        data = []
        for user in self.users_model.users:
            u = {
                "full_name": user.full_name,
                "phone_number": user.phone_number,
                "address": user.address,
                "orders": []
            }
            for order in user.orders:
                o = [{"name": p.name, "quantity": p.quantity} for p in order.products]
                u["orders"].append(o)
            data.append(u)
        with open("data.json", "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=4)

    # --- methods --- #
    def start_app(self):
        """
        This method start the main window.
        :return:
        """
        # טען קודם את הנתונים
        self._load_data()

        # הצג את ה־GUI
        self.menu_controller.show_menu()
        self.top_frame_controller.show_top_frame()

        # התחל את ה־listener
        self.start_listener()

        # הגדרת שמירה אוטומטית בעת סגירת חלון
        self.root.protocol("WM_DELETE_WINDOW", self.on_close)

    def display_user(self, phone_number, window):
        if not re.fullmatch(r"0\d{9}", phone_number):
            messagebox.showerror("שגיאה", "מספר הפלאפון שגוי", parent=window)
            return
        user = self.users_model.is_user_exist(phone_number)
        if user is None:
            messagebox.showerror("שגיאה", "מספר הפלאפון לא נמצא", parent=window)
            return
        self.top_frame_controller.update_top_frame(user.full_name, user.phone_number, user.address)
        self.orders_view.create(user)
        window.destroy()

    def clear_user(self):
        self.top_frame_controller.clear_user()
        self.orders_view.clear()

    def add_order(self, phone_number, name, product_dict, time, window):
        # is
        if not re.fullmatch(r"0\d{9}", phone_number):
            messagebox.showerror("שגיאה", "מספר הפלאפון שגוי", parent=window)
            return
        user = self.users_model.is_user_exist(phone_number)
        if user is None:
            messagebox.showerror("שגיאה", "מספר הפלאפון לא נמצא", parent=window)
            return
        new_order = Order(time)
        for name, quantity in product_dict.items():
            new_order.add_product(name, quantity)
        user.orders.append(new_order)
        messagebox.showinfo("הודעה", "ההזמנה נוספה בהצלחה", parent=window)
        window.destroy()

    def run_listener(self):
        phone_ip = "192.168.15.12"
        pc_ip = "192.168.15.10"

        # פונקציה שתטפל בכל חבילה
        def handle_packet(pkt):
            if pkt.haslayer('UDP') and pkt.haslayer('Raw'):
                print("[+] Received UDP packet")
                data = pkt['Raw'].load.decode(errors='ignore')
                if "INVITE sip:" in data:
                    # חילוץ המספר שמתקשרים אליו (Called Number)
                    start = data.find("INVITE sip:") + len("INVITE sip:")
                    end = data.find("@", start)
                    number = data[start:end]

                    # חילוץ ה-Caller ID מתוך From:
                    caller = ""
                    if "From:" in data:
                        f_start = data.find("From:") + len("From:")
                        f_end = data.find("\r\n", f_start)
                        caller = data[f_start:f_end].strip()

                    print(f"נכנסת שיחה! Caller: {caller}, Called: {number}")
                    # מפעיל GUI בדרך בטוחה מתוך ה-Main Thread
                    self.root.after(0, self.show_caller_frame, number)

        # מתחיל לקלוט חבילות בזמן אמת
        # -sniff- is a function that allows you to “capture” network packets in real time,
        #         meaning it listens to all the packets passing through your network interface and lets you process them as needed.
        # SIP works in port 5060
        # one of them is phone_ip (destination or target)
        sniff(filter=f"host {phone_ip} and udp port 5060", prn=handle_packet)

        # ((ip.src == 192.168.15.12 && ip.dst == 192.168.15.10) || (ip.src == 192.168.15.10 && ip.dst == 192.168.15.12))
        # Installing Npcap

    def start_listener(self):
        t1 = threading.Thread(target=self.run_listener)
        t1.start()

    def show_caller_frame(self, phone_number):
        # create frame
        user_frame = tk.Toplevel(self.root)
        user_frame.title("PizzaPop - Called User")
        user_frame.state("zoomed")
        user_frame.configure(bg="green")

        # --- find user --- #
        user = self.users_model.is_user_exist(phone_number)
        if user is None:
            user_frame.destroy()
            return

        # --- create top frame --- #
        top_frame_view = TopFrameView(user_frame)
        top_frame_view.create_top_frame()
        top_frame_view.update(user.full_name, user.phone_number, user.address)
        # print(f"user: {user.full_name}, phone number: {phone_number}, address: {user.address}")
        orders_view = OrdersView(user_frame)
        orders_view.create(user, False)

