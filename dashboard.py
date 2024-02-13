import tkinter as tk
from tkinter import simpledialog, messagebox
from db_manager import DatabaseManager
from update_data import UpdateDataWindow
from financewindow import FinanceManager

class UserDatabaseDashboard:
    def __init__(self, root):
        self.root = root
        self.root.title("User Database Dashboard")

        self.root.geometry("550x200+200+100")

        self.db_manager = DatabaseManager("mydatabase.db")

        self.button_frame = tk.Frame(root)
        self.button_frame.pack(side=tk.LEFT, fill=tk.Y, padx=10, pady=10)

        self.display_frame = tk.Frame(root)
        self.display_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=10, pady=10)

        self.create_table_button = tk.Button(self.button_frame, text="Create Table", command=self.create_table)
        self.create_table_button.pack(fill=tk.X)

        self.create_profile_button = tk.Button(self.button_frame, text="Create Profile", command=self.open_profile_window)
        self.create_profile_button.pack(fill=tk.X)

        self.manage_finances_button = tk.Button(self.button_frame, text="Manage Finances", command=self.open_finance_window)
        self.manage_finances_button.pack(fill=tk.X)

        self.fetch_data_button = tk.Button(self.button_frame, text="Fetch Data", command=self.fetch_user_and_incomes_prompt)
        self.fetch_data_button.pack(fill=tk.X)


        self.update_data_button = tk.Button(self.button_frame, text="Update Data", command=self.open_update_data_window)
        self.update_data_button.pack(fill=tk.X)

        self.delete_data_button = tk.Button(self.button_frame, text="Delete Data", command=self.delete_data)
        self.delete_data_button.pack(fill=tk.X)

        self.data_display = tk.Text(self.display_frame, height=10, width=50)
        self.data_display.pack(pady=10)

    def create_table(self):
        try:
            self.db_manager.create_all_tables()
            messagebox.showinfo("Success", "All tables created successfully")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to create tables: {e}")

    def open_finance_window(self):
        new_window = tk.Toplevel()
        FinanceManager(new_window, self.db_manager)

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

    def fetch_user_and_incomes_prompt(self):
        user_id = simpledialog.askstring("Fetch Data", "Enter User ID:")
        if not user_id:
            messagebox.showwarning("Fetch Data", "User ID is required to fetch data.")
            return

        user_data = self.db_manager.fetch_data_by_user_id(user_id)
        if not user_data:
            self.data_display.delete('1.0', tk.END)
            self.data_display.insert(tk.END, "No user profile found for this ID.\n")
        else:
        
            user_fields = ['Customer ID', 'First Name', 'Last Name', 'Username', 'Password', 'Email', 'Phone Number', 'Address', 'Bio']
            formatted_user_data = "\n".join(f"{field_name}: {item}" for field_name, item in zip(user_fields, user_data))
            self.data_display.delete('1.0', tk.END)
            self.data_display.insert(tk.END, "User Profile:\n" + formatted_user_data + "\n\n")

        incomes = self.db_manager.fetch_income_data_by_user(user_id)
        if incomes:
            self.data_display.insert(tk.END, "Incomes:\n")
            income_fields = ['Income ID', 'User ID', 'Source', 'Amount', 'Date']
            for income in incomes:
                formatted_income = "\n".join(f"{field_name}: {item}" for field_name, item in zip(income_fields, income))
                self.data_display.insert(tk.END, formatted_income + "\n")
            self.data_display.insert(tk.END, "\n")
        else:
            self.data_display.insert(tk.END, "No income records found for this user.\n\n")

        expenses = self.db_manager.fetch_expense_data_by_user(user_id)
        if expenses:
            self.data_display.insert(tk.END, "Expenses:\n")
            expense_fields = ['Expense ID', 'User ID', 'Category', 'Amount', 'Date']
            for expense in expenses:
                formatted_expense = "\n".join(f"{field_name}: {item}" for field_name, item in zip(expense_fields, expense))
                self.data_display.insert(tk.END, formatted_expense + "\n")
            self.data_display.insert(tk.END, "\n")
        else:
            self.data_display.insert(tk.END, "No expense records found for this user.\n\n")

        goals = self.db_manager.fetch_goals_for_user(user_id)
        if goals:
            self.data_display.insert(tk.END, "Goals:\n")
            goal_fields = ['Goal Name', 'Target Amount', 'Start Date', 'End Date', 'Priority']
            for goal in goals:
                formatted_goal = "\n".join(f"{field_name}: {item}" for field_name, item in zip(goal_fields, goal))
                self.data_display.insert(tk.END, formatted_goal + "\n\n")
        else:
            self.data_display.insert(tk.END, "No goal records found for this user.\n\n")

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