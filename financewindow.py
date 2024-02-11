import tkinter as tk
from tkinter import messagebox

class FinanceManager:
    def __init__(self, root, db_manager):
        self.root = root
        self.db_manager = db_manager
        self.root.title("Finance Manager")

        # Setup the main interface with buttons to choose the section to manage
        tk.Button(self.root, text="Manage Incomes", command=self.setup_income_form).grid(row=0, column=0, padx=10, pady=10)
        tk.Button(self.root, text="Manage Expenses", command=self.setup_expense_form).grid(row=0, column=1, padx=10, pady=10)
        tk.Button(self.root, text="Manage Budgets", command=self.setup_budget_form).grid(row=0, column=2, padx=10, pady=10)

        # Placeholder frame for dynamic form content
        self.form_frame = tk.Frame(self.root)
        self.form_frame.grid(row=1, column=0, columnspan=3, sticky="ew")

    def clear_form(self):
        """Clear existing form content."""
        for widget in self.form_frame.winfo_children():
            widget.destroy()

    def setup_income_form(self):
        """Setup form fields and buttons for managing incomes."""
        self.clear_form()
        
        # Example setup for income form fields and buttons
        tk.Label(self.form_frame, text="User ID:").grid(row=0, column=0, padx=10, pady=5)
        self.user_id_entry = tk.Entry(self.form_frame)
        self.user_id_entry.grid(row=0, column=1, padx=10, pady=5)

        tk.Label(self.form_frame, text="Income Source:").grid(row=1, column=0, padx=10, pady=5)
        self.income_source_entry = tk.Entry(self.form_frame)
        self.income_source_entry.grid(row=1, column=1, padx=10, pady=5)

        tk.Label(self.form_frame, text="Income Amount:").grid(row=2, column=0, padx=10, pady=5)
        self.income_amount_entry = tk.Entry(self.form_frame)
        self.income_amount_entry.grid(row=2, column=1, padx=10, pady=5)

        tk.Label(self.form_frame, text="Income Date (YYYY-MM-DD):").grid(row=3, column=0, padx=10, pady=5)
        self.income_date_entry = tk.Entry(self.form_frame)
        self.income_date_entry.grid(row=3, column=1, padx=10, pady=5)

        tk.Button(self.form_frame, text="Save Income", command=self.save_income).grid(row=4, column=0, padx=10, pady=10)
        tk.Button(self.form_frame, text="Update Income", command=self.update_income).grid(row=4, column=1, padx=10, pady=10)
        tk.Button(self.form_frame, text="Delete Income", command=self.delete_income).grid(row=4, column=2, padx=10, pady=10)

    def setup_expense_form(self):
        """Setup form fields and buttons for managing expenses."""
        self.clear_form()
        # Implement similarly to setup_income_form, adjusted for expenses

    def setup_budget_form(self):
        """Setup form fields and buttons for managing budgets."""
        self.clear_form()
        # Implement similarly to setup_income_form, adjusted for budgets

    def save_income(self):
        """Save income data to the database."""
        # Example implementation
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
        """Update existing income data."""
        # Implement based on your application's requirements

    def delete_income(self):
        """Delete an income record."""
        # Implement based on your application's requirements

    def validate_data(self, data):
        """Validate form data."""
        try:
            if not all(data.values()) or float(data['amount']) <= 0:
                return False
            return True
        except ValueError:
            return False
        
        
    def setup_expense_form(self):
        """Setup form fields and buttons for managing expenses."""
        self.clear_form()
        
        tk.Label(self.form_frame, text="User ID:").grid(row=0, column=0, padx=10, pady=5)
        self.expense_user_id_entry = tk.Entry(self.form_frame)
        self.expense_user_id_entry.grid(row=0, column=1, padx=10, pady=5)

        tk.Label(self.form_frame, text="Expense Category:").grid(row=1, column=0, padx=10, pady=5)
        self.expense_category_entry = tk.Entry(self.form_frame)
        self.expense_category_entry.grid(row=1, column=1, padx=10, pady=5)

        tk.Label(self.form_frame, text="Expense Amount:").grid(row=2, column=0, padx=10, pady=5)
        self.expense_amount_entry = tk.Entry(self.form_frame)
        self.expense_amount_entry.grid(row=2, column=1, padx=10, pady=5)

        tk.Label(self.form_frame, text="Expense Date (YYYY-MM-DD):").grid(row=3, column=0, padx=10, pady=5)
        self.expense_date_entry = tk.Entry(self.form_frame)
        self.expense_date_entry.grid(row=3, column=1, padx=10, pady=5)

        tk.Button(self.form_frame, text="Save Expense", command=self.save_expense).grid(row=4, column=0, padx=10, pady=10)
        tk.Button(self.form_frame, text="Update Expense", command=self.update_expense).grid(row=4, column=1, padx=10, pady=10)
        tk.Button(self.form_frame, text="Delete Expense", command=self.delete_expense).grid(row=4, column=2, padx=10, pady=10)

    def save_expense(self):
        """Save expense data to the database."""
        user_id = self.expense_user_id_entry.get()
        category = self.expense_category_entry.get()
        amount = self.expense_amount_entry.get()
        date = self.expense_date_entry.get()

        if not self.validate_data({'user_id': user_id, 'category': category, 'amount': amount, 'date': date}):
            messagebox.showwarning("Warning", "Invalid data. Please correct and try again.")
            return

        try:
            self.db_manager.add_expense(user_id, category, amount, date)
            messagebox.showinfo("Success", "Expense saved successfully")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to save expense: {e}")

    def update_expense(self):
        """Update an existing expense record."""
        # Implement based on your application's requirements

    def delete_expense(self):
        """Delete an expense record."""
        # Implement based on your application's requirements

    # Placeholder for the validate_data method
    def validate_data(self, data):
        try:
            if not all(data.values()) or float(data['amount']) <= 0:
                return False
            return True
        except ValueError:
            return False
# Example usage
if __name__ == "__main__":
    root = tk.Tk()
    db_manager = None  # Replace with your actual DatabaseManager instance
    app = FinanceManager(root, db_manager)
    root.mainloop()
