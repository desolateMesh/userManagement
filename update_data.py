import tkinter as tk
from tkinter import messagebox
from db_manager import DatabaseManager


class UpdateDataWindow:
    def __init__(self, root, db_manager):
        self.root = root
        self.root.title("Update Data")

        self.db_manager = db_manager

        tk.Label(root, text="Customer ID:").pack()
        self.customer_id_entry = tk.Entry(root)
        self.customer_id_entry.pack(fill=tk.X)

        tk.Label(root, text="Username:").pack()
        self.username_entry = tk.Entry(root)
        self.username_entry.pack(fill=tk.X)

        tk.Label(root, text="Password:").pack()
        self.password_entry = tk.Entry(root, show="*")
        self.password_entry.pack(fill=tk.X)

        tk.Label(root, text="First Name:").pack()
        self.first_name_entry = tk.Entry(root)
        self.first_name_entry.pack(fill=tk.X)

        tk.Label(root, text="Last Name:").pack()
        self.last_name_entry = tk.Entry(root)
        self.last_name_entry.pack(fill=tk.X)

        tk.Label(root, text="Email:").pack()
        self.email_entry = tk.Entry(root)
        self.email_entry.pack(fill=tk.X)

        tk.Label(root, text="Phone Number:").pack()
        self.phone_number_entry = tk.Entry(root)
        self.phone_number_entry.pack(fill=tk.X)

        tk.Label(root, text="Address:").pack()
        self.address_entry = tk.Entry(root)
        self.address_entry.pack(fill=tk.X)

        tk.Label(root, text="Bio:").pack()
        self.bio_entry = tk.Entry(root)
        self.bio_entry.pack(fill=tk.X)

        self.update_button = tk.Button(root, text="Update Profile", command=self.update_profile)
        self.update_button.pack(fill=tk.X)

    def update_profile(self):
        customer_id = self.customer_id_entry.get()
        new_data = {
            "username": self.username_entry.get(),
            "password": self.password_entry.get(),
            "first_name": self.first_name_entry.get(),
            "last_name": self.last_name_entry.get(),
            "email": self.email_entry.get(),
            "phone_number": self.phone_number_entry.get(),
            "address": self.address_entry.get(),
            "bio": self.bio_entry.get()
        }

        if customer_id:
            try:
                self.db_manager.update_partial_data(customer_id, new_data)
                messagebox.showinfo("Info", "Profile Updated")
                self.root.destroy()
            except Exception as e:
                messagebox.showerror("Error", str(e))
        else:
            messagebox.showwarning("Warning", "Please provide a Customer ID.")

def main():
    root = tk.Tk()
    app = UpdateDataWindow(root)
    root.mainloop()

if __name__ == "__main__":
    main()