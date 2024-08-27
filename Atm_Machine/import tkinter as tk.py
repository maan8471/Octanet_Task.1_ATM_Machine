import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

class ATMApp:
    def __init__(self, root):
        self.root = root
        self.root.title("ATM Machine")
        self.root.geometry("500x400")
        self.balance = 1000  # Starting balance
        self.pin = "1234"    # Default PIN

        self.background_image = Image.open("background.jpg")
        self.background_photo = ImageTk.PhotoImage(self.background_image)

        self.create_login_screen()

    def create_login_screen(self):
        self.clear_screen()
        self.add_background()

        self.login_frame = tk.Frame(self.root, bg="lightblue")
        self.login_frame.place(relwidth=0.8, relheight=0.6, relx=0.1, rely=0.2)

        tk.Label(self.login_frame, text="Enter PIN:", font=("Arial", 14), bg="lightblue").pack(pady=10)
        self.pin_entry = tk.Entry(self.login_frame, show="*", font=("Arial", 14))
        self.pin_entry.pack(pady=10)
        tk.Button(self.login_frame, text="Login", font=("Arial", 14), command=self.login).pack(pady=10)

    def login(self):
        entered_pin = self.pin_entry.get()
        if entered_pin == self.pin:
            self.create_main_menu()
        else:
            messagebox.showerror("Error", "Invalid PIN")

    def create_main_menu(self):
        self.clear_screen()
        self.add_background()

        self.main_menu_frame = tk.Frame(self.root, bg="lightgreen")
        self.main_menu_frame.place(relwidth=0.8, relheight=0.6, relx=0.1, rely=0.2)

        tk.Label(self.main_menu_frame, text="ATM Menu", font=("Arial", 18), bg="lightgreen").pack(pady=10)
        tk.Button(self.main_menu_frame, text="Check Balance", font=("Arial", 14), command=self.check_balance).pack(pady=10)
        tk.Button(self.main_menu_frame, text="Credit", font=("Arial", 14), command=self.credit_money).pack(pady=10)
        tk.Button(self.main_menu_frame, text="Debit", font=("Arial", 14), command=self.debit_money).pack(pady=10)
        tk.Button(self.main_menu_frame, text="Change PIN", font=("Arial", 14), command=self.change_pin).pack(pady=10)
        tk.Button(self.main_menu_frame, text="Logout", font=("Arial", 14), command=self.create_login_screen).pack(pady=10)

    def check_balance(self):
        messagebox.showinfo("Balance", f"Current Balance: ${self.balance}")

    def credit_money(self):
        self.clear_screen()
        self.add_background()

        tk.Label(self.root, text="Enter amount to credit:", font=("Arial", 14), bg="lightyellow").pack(pady=10)
        self.credit_entry = tk.Entry(self.root, font=("Arial", 14))
        self.credit_entry.pack(pady=10)
        tk.Button(self.root, text="Submit", font=("Arial", 14), command=self.submit_credit).pack(pady=10)

    def submit_credit(self):
        amount = self.credit_entry.get()
        try:
            amount = float(amount)
            if amount > 0:
                self.balance += amount
                messagebox.showinfo("Success", f"Credited ${amount}. New Balance: ${self.balance}")
                self.create_main_menu()
            else:
                messagebox.showerror("Error", "Amount must be greater than 0")
        except ValueError:
            messagebox.showerror("Error", "Invalid amount")

    def debit_money(self):
        self.clear_screen()
        self.add_background()

        tk.Label(self.root, text="Enter amount to debit:", font=("Arial", 14), bg="lightcoral").pack(pady=10)
        self.debit_entry = tk.Entry(self.root, font=("Arial", 14))
        self.debit_entry.pack(pady=10)
        tk.Button(self.root, text="Submit", font=("Arial", 14), command=self.submit_debit).pack(pady=10)

    def submit_debit(self):
        amount = self.debit_entry.get()
        try:
            amount = float(amount)
            if amount > 0 and amount <= self.balance:
                self.balance -= amount
                messagebox.showinfo("Success", f"Debited ${amount}. New Balance: ${self.balance}")
                self.create_main_menu()
            elif amount > self.balance:
                messagebox.showerror("Error", "Insufficient funds")
            else:
                messagebox.showerror("Error", "Amount must be greater than 0")
        except ValueError:
            messagebox.showerror("Error", "Invalid amount")

    def change_pin(self):
        self.clear_screen()
        self.add_background()

        tk.Label(self.root, text="Enter new PIN:", font=("Arial", 14), bg="lightblue").pack(pady=10)
        self.new_pin_entry = tk.Entry(self.root, show="*", font=("Arial", 14))
        self.new_pin_entry.pack(pady=10)
        tk.Button(self.root, text="Submit", font=("Arial", 14), command=self.submit_pin_change).pack(pady=10)

    def submit_pin_change(self):
        new_pin = self.new_pin_entry.get()
        if len(new_pin) == 4 and new_pin.isdigit():
            self.pin = new_pin
            messagebox.showinfo("Success", "PIN changed successfully")
            self.create_main_menu()
        else:
            messagebox.showerror("Error", "PIN must be a 4-digit number")

    def clear_screen(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    def add_background(self):
        background_label = tk.Label(self.root, image=self.background_photo)
        background_label.place(relwidth=1, relheight=1)

if __name__ == "__main__":
    root = tk.Tk()
    app = ATMApp(root)
    root.mainloop()
