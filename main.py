import tkinter as tk
from dashboard import UserDatabaseDashboard
from db_manager import DatabaseManager


def main():

    db_name = "mydatabase.db" 
    db_manager = DatabaseManager(db_name)
    db_manager.create_all_tables()
    
    root = tk.Tk()
    app = UserDatabaseDashboard(root)
    root.mainloop()

if __name__ == "__main__":
    main()
    