import sqlite3

class DatabaseManager:
    def __init__(self, db_name):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()

    def create_all_tables(self):
        self.create_user_table()
        self.create_income_table()
        self.create_budget_table()
        self.create_expense_table()
        self.create_goals_table()

    def create_user_table(self):
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS user (
                               user_id TEXT PRIMARY KEY,
                               first_name TEXT NOT NULL,
                               last_name TEXT NOT NULL,
                               username TEXT NOT NULL,
                               password TEXT NOT NULL,
                               email TEXT NOT NULL,
                               phone_number TEXT NOT NULL,
                               address TEXT,
                               bio TEXT)""")
        self.conn.commit()

    def create_income_table(self):
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS income (
                               income_id INTEGER PRIMARY KEY AUTOINCREMENT,
                               user_id TEXT,
                               source TEXT,
                               amount REAL,
                               date TEXT,
                               FOREIGN KEY(user_id) REFERENCES user(user_id))""")
        self.conn.commit()

    def create_budget_table(self):
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS budget (
                               budget_id INTEGER PRIMARY KEY AUTOINCREMENT,
                               user_id TEXT,
                               category TEXT,
                               amount REAL,
                               start_date TEXT,
                               end_date TEXT,
                               FOREIGN KEY(user_id) REFERENCES user(user_id))""")
        self.conn.commit()

    def create_expense_table(self):
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS expense (
                               expense_id INTEGER PRIMARY KEY AUTOINCREMENT,
                               user_id TEXT,
                               category TEXT,
                               amount REAL,
                               date TEXT,
                               FOREIGN KEY(user_id) REFERENCES user(user_id))""")
        self.conn.commit()

    def create_goals_table(self):
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS goals (
                                goal_id INTEGER PRIMARY KEY AUTOINCREMENT,
                                user_id TEXT,
                                goal_name TEXT NOT NULL,
                                target_amount REAL NOT NULL,
                                start_date TEXT NOT NULL,
                                end_date TEXT NOT NULL,
                                priority INTEGER CHECK(priority BETWEEN 1 AND 5),
                                FOREIGN KEY(user_id) REFERENCES user(user_id))""")
        self.conn.commit()

    def add_income(self, user_id, source, amount, date):
        query = """INSERT INTO income (user_id, source, amount, date) VALUES (?, ?, ?, ?)"""
        self.cursor.execute(query, (user_id, source, amount, date))
        self.conn.commit()

    def update_income(self, income_id, source, amount, date):
        query = """UPDATE income SET source=?, amount=?, date=? WHERE income_id=?"""
        self.cursor.execute(query, (source, amount, date, income_id))
        self.conn.commit()

    def delete_income(self, income_id):
        query = """DELETE FROM income WHERE income_id=?"""
        self.cursor.execute(query, (income_id,))
        self.conn.commit()

    def create_profile(self, user_data):
        try:
            self.cursor.execute("""INSERT INTO user (user_id, first_name, last_name, username, password, email, phone_number, address, bio)
                                   VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)""", user_data)
            self.conn.commit()
            print("Profile created successfully")
        except Exception as e:
            print(f"Error creating profile: {str(e)}")

    def fetch_data_by_user_id(self, user_id):
        try:
            self.cursor.execute("SELECT * FROM user WHERE user_id=?", (user_id,))
            return self.cursor.fetchone()
        except Exception as e:
            print(f"Error fetching user data for user_id {user_id}: {str(e)}")
            return None

    def fetch_income_data_by_user(self, user_id):
        try:
            self.cursor.execute("SELECT * FROM income WHERE user_id=?", (user_id,))
            incomes = self.cursor.fetchall()
            return incomes
        except Exception as e:
            print(f"Error fetching income data for user {user_id}: {str(e)}")
            return []

    def fetch_data(self):
        try:
            self.cursor.execute("SELECT * FROM user")
            return self.cursor.fetchall()
        except Exception as e:
            print(f"Error fetching data: {str(e)}")
            return []

    def update_data(self, user_id, updated_data):
        try:
            self.cursor.execute("""UPDATE user SET 
                                   first_name=?, last_name=?, username=?, password=?, email=?, phone_number=?, address=?, bio=? 
                                   WHERE user_id=?""", updated_data + (user_id,))
            self.conn.commit()
            print("Profile updated successfully")
        except Exception as e:
            print(f"Error updating profile: {str(e)}")

    def update_partial_data(self, user_id, new_data):
       
        filtered_data = {k: v for k, v in new_data.items() if v}
        updates = ", ".join(f"{key} = ?" for key in filtered_data.keys())
        sql = f"UPDATE user SET {updates} WHERE user_id = ?"

        params = list(filtered_data.values()) + [user_id]

        try:
            self.cursor.execute(sql, params)
            self.conn.commit()
        except Exception as e:
            print(f"Error updating data: {e}")
            raise

    def delete_data(self, user_id):
        try:
            self.cursor.execute("DELETE FROM user WHERE user_id=?", (user_id,))
            self.conn.commit()
            print("Profile deleted successfully")
        except Exception as e:
            print(f"Error deleting profile: {str(e)}")

    def add_expense(self, user_id, category, amount, date):
        """Add a new expense record to the database."""
        try:
            self.cursor.execute("""INSERT INTO expense (user_id, category, amount, date) 
                                   VALUES (?, ?, ?, ?)""", (user_id, category, amount, date))
            self.conn.commit()
        except Exception as e:
            print(f"Error adding expense: {str(e)}")

    def update_expense(self, expense_id, category, amount, date):
        """Update an existing expense record."""
        try:
            self.cursor.execute("""UPDATE expense SET category=?, amount=?, date=? 
                                   WHERE expense_id=?""", (category, amount, date, expense_id))
            self.conn.commit()
        except Exception as e:
            print(f"Error updating expense: {str(e)}")

    def delete_expense(self, expense_id):
        """Delete an expense record from the database."""
        try:
            self.cursor.execute("DELETE FROM expense WHERE expense_id=?", (expense_id,))
            self.conn.commit()
        except Exception as e:
            print(f"Error deleting expense: {str(e)}")

    def fetch_expense_data_by_user(self, user_id):
        try:
            self.cursor.execute("SELECT * FROM expense WHERE user_id=?", (user_id,))
            expense = self.cursor.fetchall()
            return expense
        except Exception as e:
            print(f"Error fetching expense data for user {user_id}: {str(e)}")
            return []

    def fetch_income_and_expense_for_user(self, user_id):
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM income WHERE user_id=?", (user_id,))
        income = cursor.fetchall()
        cursor.execute("SELECT * FROM expense WHERE user_id=?", (user_id,))
        expense = cursor.fetchall()
        cursor.execute("SELECT goal_name, target_amount FROM goals WHERE user_id=?", (user_id,))
        goals = cursor.fetchall()
        return income, expense, goals
    
    def add_goal(self, user_id, goal_name, target_amount, start_date, end_date, priority):
        self.cursor.execute("""INSERT INTO goals (user_id, goal_name, target_amount, start_date, end_date, priority) 
                            VALUES (?, ?, ?, ?, ?, ?)""",
                            (user_id, goal_name, target_amount, start_date, end_date, priority))
        self.conn.commit()
        
    def fetch_goals_for_user(self, user_id):
        self.cursor.execute("SELECT goal_name, target_amount, start_date, end_date, priority FROM goals WHERE user_id=?", (user_id,))
        return self.cursor.fetchall()

