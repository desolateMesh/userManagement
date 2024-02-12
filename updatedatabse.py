import sqlite3

def update_database(db_name):
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS user (
                       user_id TEXT PRIMARY KEY,
                       first_name TEXT NOT NULL,
                       last_name TEXT NOT NULL,
                       username TEXT NOT NULL,
                       password TEXT NOT NULL,
                       email TEXT NOT NULL,
                       phone_number TEXT NOT NULL,
                       address TEXT,
                       bio TEXT)""")

    cursor.execute("""CREATE TABLE IF NOT EXISTS income (
                       income_id INTEGER PRIMARY KEY AUTOINCREMENT,
                       user_id TEXT,
                       source TEXT,
                       amount REAL,
                       date TEXT,
                       FOREIGN KEY(user_id) REFERENCES user(user_id))""")

    cursor.execute("""CREATE TABLE IF NOT EXISTS budget (
                       budget_id INTEGER PRIMARY KEY AUTOINCREMENT,
                       user_id TEXT,
                       category TEXT,
                       amount REAL,
                       start_date TEXT,
                       end_date TEXT,
                       FOREIGN KEY(user_id) REFERENCES user(user_id))""")

    cursor.execute("""CREATE TABLE IF NOT EXISTS expense (
                       expense_id INTEGER PRIMARY KEY AUTOINCREMENT,
                       user_id TEXT,
                       category TEXT,
                       amount REAL,
                       date TEXT,
                       FOREIGN KEY(user_id) REFERENCES user(user_id))""")

    cursor.execute("""CREATE TABLE IF NOT EXISTS goals (
                       goal_id INTEGER PRIMARY KEY AUTOINCREMENT,
                       user_id TEXT,
                       goal_name TEXT NOT NULL,
                       target_amount REAL NOT NULL,
                       start_date TEXT NOT NULL,
                       end_date TEXT NOT NULL,
                       priority INTEGER CHECK(priority BETWEEN 1 AND 5),
                       FOREIGN KEY(user_id) REFERENCES user(user_id))""")

    print("Database tables created or updated successfully.")
    conn.commit()
    conn.close()

if __name__ == "__main__":
    db_name = "mydatabase.db"
    update_database(db_name)
