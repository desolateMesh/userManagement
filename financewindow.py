import tkinter as tk
from tkinter import messagebox
from tkinter import simpledialog
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class FinanceManager:
    def __init__(self, root, db_manager):
        self.root = root
        self.db_manager = db_manager
        self.root.title("Finance Manager")

        tk.Button(self.root, text="Manage Incomes", command=self.setup_income_form).grid(row=0, column=0, padx=10, pady=10)
        tk.Button(self.root, text="Manage Expenses", command=self.setup_expense_form).grid(row=0, column=1, padx=10, pady=10)
        tk.Button(self.root, text="Manage Budgets", command=self.prompt_user_id_and_open_budget_window).grid(row=0, column=2, padx=10, pady=10)

        self.form_frame = tk.Frame(self.root)
        self.form_frame.grid(row=1, column=0, columnspan=3, sticky="ew")

    def clear_form(self):
        """Clear existing form content."""
        for widget in self.form_frame.winfo_children():
            widget.destroy()

    def setup_income_form(self):
        """Setup form fields and buttons for managing incomes."""
        self.clear_form()
        
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
        
    def save_income(self):
        """Save income data to the database."""
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
        
    def delete_income(self):
        """Delete an income record."""

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
        
    def delete_expense(self):
        """Delete an expense record."""
       
    def validate_data(self, data):
        try:
            if not all(data.values()) or float(data['amount']) <= 0:
                return False
            return True
        except ValueError:
            return False

    def prompt_user_id_and_open_budget_window(self):
        user_id = simpledialog.askstring("Manage Budgets", "Enter User ID:")
        if user_id:
            self.open_budget_window(user_id)
        else:
            messagebox.showwarning("Manage Budgets", "User ID is required.")

    def open_budget_window(self, user_id):
        self.root.destroy()          
        budget_window = tk.Tk()
        budget_window.title("Manage Budgets for User ID: " + user_id)

        income, expense = self.db_manager.fetch_income_and_expense_for_user(user_id)
        self.setup_budget_management_interface(budget_window, income, expense)

    def setup_budget_management_interface(self, budget_window, incomes, expenses):
        total_income = sum(income[3] for income in incomes) if incomes else 0
        total_expense = sum(expense[3] for expense in expenses) if expenses else 0
        remaining_budget = total_income - total_expense

        labels = ['Income', 'Expense', 'Remaining Budget']
        sizes = [total_income, total_expense, remaining_budget]
        colors = ['gold', 'yellowgreen', 'lightcoral']

        fig1, ax1 = plt.subplots()
        ax1.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=140)
        ax1.axis('equal')

        canvas = FigureCanvasTkAgg(fig1, master=budget_window)
        canvas.draw()
        canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

        tk.Button(budget_window, text="Button1").pack()
        tk.Button(budget_window, text="Button2").pack()
        tk.Button(budget_window, text="Button3").pack()
    
    plt.show()


if __name__ == "__main__":
    root = tk.Tk()
    db_manager = None  
    app = FinanceManager(root, db_manager)
    root.mainloop()
