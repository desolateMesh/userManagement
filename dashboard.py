import tkinter as tk
from tkinter import simpledialog, messagebox
from db_manager import DatabaseManager
from update_data import UpdateDataWindow

class UserDatabaseDashboard:
    def __init__(self, root):
        self.root = root
        self.root.title("User Database Dashboard")
        self.db_manager = DatabaseManager("mydatabase.db")

        self.button_frame = tk.Frame(root)
        self.button_frame.pack(side=tk.LEFT, fill=tk.Y, padx=10, pady=10)

        self.display_frame = tk.Frame(root)
        self.display_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=10, pady=10)

        self.create_table_button = tk.Button(self.button_frame, text="Create Table", command=self.create_table)
        self.create_table_button.pack(fill=tk.X)

        self.create_profile_button = tk.Button(self.button_frame, text="Create Profile", command=self.open_profile_window)
        self.create_profile_button.pack(fill=tk.X)

        self.fetch_data_button = tk.Button(self.button_frame, text="Fetch Data", command=self.fetch_data)
        self.fetch_data_button.pack(fill=tk.X)

        self.update_data_button = tk.Button(self.button_frame, text="Update Data", command=self.open_update_data_window)
        self.update_data_button.pack(fill=tk.X)

        self.delete_data_button = tk.Button(self.button_frame, text="Delete Data", command=self.delete_data)
        self.delete_data_button.pack(fill=tk.X)

        self.data_display = tk.Text(self.display_frame, height=10, width=50)
        self.data_display.pack(pady=10)

    def create_table(self):
        self.db_manager.create_customer_table()

    def open_profile_window(self):
        profile_window = tk.Toplevel(self.root)
        profile_window.title("Create Profile")
        labels = ['Customer ID', 'First Name', 'Last Name', 'Username', 'Password', 'Email', 'Phone Number', 'Address', 'Bio']
        entries = {}
        for i, label in enumerate(labels):
            tk.Label(profile_window, text=label).grid(row=i, column=0)
            entry = tk.Entry(profile_window)
            entry.grid(row=i, column=1)
            entries[label] = entry

        def save_profile():
            profile_data = tuple(entries[label].get() for label in labels)
            self.db_manager.create_profile(profile_data)
            profile_window.destroy()

        save_button = tk.Button(profile_window, text="Save Profile", command=save_profile)
        save_button.grid(row=len(labels), column=0, columnspan=2)

    def fetch_data(self):
        data = self.db_manager.fetch_data()
        self.data_display.delete('1.0', tk.END)

        for row in data:
            formatted_row = "\n".join(f"{field_name}: {item}" for field_name, item in zip(['Customer ID', 'First Name', 'Last Name', 'Username', 'Password', 'Email', 'Phone Number', 'Address', 'Bio'], row))
            self.data_display.insert(tk.END, formatted_row + "\n\n")

    def open_update_data_window(self):
        update_window = tk.Toplevel(self.root)
        update_data_window = UpdateDataWindow(update_window, self.db_manager)

    def delete_data(self):
        customer_id = simpledialog.askstring("Delete Profile", "Enter Customer ID:")
        if customer_id:
            self.db_manager.delete_data(customer_id)
            messagebox.showinfo("Success", "Profile deleted successfully")

if __name__ == "__main__":
    root = tk.Tk()
    app = UserDatabaseDashboard(root)
    root.mainloop()