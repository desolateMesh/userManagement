import tkinter as tk
from dashboard import UserDatabaseDashboard
from db_manager import DatabaseManager


def main():
    root = tk.Tk()
    app = UserDatabaseDashboard(root)
    root.mainloop()

if __name__ == "__main__":
    main()