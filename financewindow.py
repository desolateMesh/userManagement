import tkinter as tk
from tkinter import messagebox
from tkinter import simpledialog
from datetime import datetime
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from itertools import cycle

class FinanceManager:
    def __init__(self, root, db_manager):
        self.root = root
        self.db_manager = db_manager
        self.root.title("Finance Manager")

        self.root.geometry("550x200+200+100")

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

    def open_budget_window(self, username):
        self.root.destroy()          
        budget_window = tk.Tk()
        budget_window.title("Manage Budgets for User ID: " + username)

        income, expense = self.db_manager.fetch_income_and_expense_for_user(username)
        self.setup_budget_management_interface(budget_window, income, expense)

    def setup_budget_management_interface(self, budget_window, incomes, expenses):
    
        income_dict = {}
        for income in incomes if incomes else []:
            income_dict[income[2]] = income_dict.get(income[2], 0) + income[3]

        expense_dict = {}
        for expense in expenses if expenses else []:
            expense_dict[expense[2]] = expense_dict.get(expense[2], 0) + expense[3]

        total_income = sum(income_dict.values())
        total_expense = sum(expense_dict.values())
        remaining_budget = total_income - total_expense

        labels = list(income_dict.keys()) + list(expense_dict.keys()) + ['Remaining Budget']
        sizes = list(income_dict.values()) + list(expense_dict.values()) + [remaining_budget]

        base_colors = ['gold', 'yellowgreen', 'lightcoral', 'skyblue', 'orange', 'purple', 'pink', 'lightblue', 'lightgreen', 'grey']
        color_cycle = cycle(base_colors)
        colors = [next(color_cycle) for _ in range(len(labels))]

        fig, ax1 = plt.subplots()
        ax1.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=140)
        ax1.axis('equal')  

        canvas = FigureCanvasTkAgg(fig, master=budget_window)
        canvas.draw()
        canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

        button_frame = tk.Frame(budget_window)
        button_frame.pack(side=tk.BOTTOM, pady=10)

        tk.Button(button_frame, text="New Budget Goal", command=self.create_new_budget_goal).pack(side=tk.LEFT, padx=5)        
        tk.Button(button_frame, text="Update Budget Goal").pack(side=tk.LEFT, padx=5)
        tk.Button(button_frame, text="Delete Budget Goal").pack(side=tk.LEFT, padx=5)
        tk.Button(button_frame, text="Back").pack(side=tk.LEFT, padx=5)

        plt.close(fig)


    def create_new_budget_goal(self):
        goal_window = tk.Toplevel()
        goal_window.title("Set New Budget Goal")

        tk.Label(goal_window, text="User ID:").grid(row=0, column=0)
        user_id_entry = tk.Entry(goal_window)
        user_id_entry.grid(row=0, column=1)

        tk.Label(goal_window, text="Goal Name:").grid(row=1, column=0)
        goal_name_entry = tk.Entry(goal_window)
        goal_name_entry.grid(row=1, column=1)

        tk.Label(goal_window, text="Goal Amount to be saved:").grid(row=2, column=0)
        goal_amount_entry = tk.Entry(goal_window)
        goal_amount_entry.grid(row=2, column=1)

        tk.Label(goal_window, text="Goal Timeline Start:").grid(row=3, column=0)
        goal_start_entry = tk.Entry(goal_window)
        goal_start_entry.grid(row=3, column=1)

        tk.Label(goal_window, text="Goal Timeline End:").grid(row=4, column=0)
        goal_end_entry = tk.Entry(goal_window)
        goal_end_entry.grid(row=4, column=1)

        tk.Label(goal_window, text="Priority (1-5):").grid(row=5, column=0)
        priority_entry = tk.Entry(goal_window)
        priority_entry.grid(row=5, column=1)

        submit_button = tk.Button(goal_window, text="Submit Goal",
                                command=lambda: self.submit_goal(
                                    user_id_entry.get(),
                                    goal_name_entry.get(),
                                    goal_amount_entry.get(),
                                    goal_start_entry.get(),
                                    goal_end_entry.get(),
                                    priority_entry.get()))
        submit_button.grid(row=6, column=0, columnspan=2)


    def submit_goal(self, user_id, name, amount, start, end, priority):
        try:
            amount = float(amount)
            if amount <= 0:
                raise ValueError("Amount must be positive.")
        
            start_date = datetime.strptime(start, "%Y-%m-%d")
            end_date = datetime.strptime(end, "%Y-%m-%d")
            if start_date >= end_date:
                raise ValueError("Start date must be before end date.")
            if start_date < datetime.now():
                raise ValueError("Start date cannot be in the past.")

            priority = int(priority)  
            if priority < 1 or priority > 5:
                raise ValueError("Priority must be between 1 and 5.")

            self.db_manager.add_goal(user_id, name, amount, start, end, priority)

            messagebox.showinfo("Success", "Goal added successfully.")
        except ValueError as e:

            messagebox.showerror("Error", f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    root = tk.Tk()
    db_manager = None  
    app = FinanceManager(root, db_manager)
    root.mainloop()