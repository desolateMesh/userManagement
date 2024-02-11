import tkinter as tk
from tkinter import ttk, messagebox

class FinanceManager:
    def __init__(self, root, db_manager):
        self.root = root
        self.db_manager = db_manager
        self.root.title("Finance Manager")

        self.setup_income_form()

    def setup_income_form(self):

        tk.Label(self.root, text="User ID:").grid(row=0, column=0, padx=10, pady=5)
        self.user_id_entry = tk.Entry(self.root)
        self.user_id_entry.grid(row=0, column=1, padx=10, pady=5)

        tk.Label(self.root, text="Income Source:").grid(row=1, column=0, padx=10, pady=5)
        self.income_source_entry = tk.Entry(self.root)
        self.income_source_entry.grid(row=1, column=1, padx=10, pady=5)

        tk.Label(self.root, text="Income Amount:").grid(row=2, column=0, padx=10, pady=5)
        self.income_amount_entry = tk.Entry(self.root)
        self.income_amount_entry.grid(row=2, column=1, padx=10, pady=5)

        tk.Label(self.root, text="Income Date (YYYY-MM-DD):").grid(row=3, column=0, padx=10, pady=5)
        self.income_date_entry = tk.Entry(self.root)
        self.income_date_entry.grid(row=3, column=1, padx=10, pady=5)

        tk.Button(self.root, text="Save Income", command=self.save_income).grid(row=4, column=0, padx=10, pady=1)
        tk.Button(self.root, text="Update Income", command=self.update_income).grid(row=4, column=1, padx=10, pady=1)
        tk.Button(self.root, text="Delete Income", command=self.delete_income).grid(row=4, column=2, padx=10, pady=1)

    def save_income(self):
        source = self.income_source_entry.get()
        amount = self.income_amount_entry.get()
        date = self.income_date_entry.get()
        user_id = self.user_id_entry.get() 
    
        if not self.validate_data({'source': source, 'amount': amount, 'date': date}):
            messagebox.showwarning("Warning", "Invalid data. Please correct and try again.")
            return
    
        try:
            self.db_manager.add_income(user_id, source, amount, date)
            messagebox.showinfo("Success", "Income saved successfully")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to save income: {e}")

    def update_income(self):
        income_id = "income_id_to_update"  
        source = self.income_source_entry.get()
        amount = self.income_amount_entry.get()
        date = self.income_date_entry.get()
    
        if not self.validate_data({'source': source, 'amount': amount, 'date': date}):
            messagebox.showwarning("Warning", "Invalid data. Please correct and try again.")
            return
        try:
            self.db_manager.update_income(income_id, (source, amount, date))
            messagebox.showinfo("Success", "Income updated successfully")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to update income: {e}")

    def delete_income(self):
        income_id = "income_id_to_delete"  
        try:
            self.db_manager.delete_income(income_id)
            messagebox.showinfo("Success", "Income deleted successfully")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to delete income: {e}")

    def validate_data(self, data):
        try:
            if not all(data.values()) or float(data['amount']) <= 0:
                return False
            return True
        except ValueError:
            return False


if __name__ == "__main__":
    root = tk.Tk()
    db_manager = None  
    app = FinanceManager(root, db_manager)
    root.mainloop()