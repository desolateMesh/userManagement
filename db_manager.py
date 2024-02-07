import sqlite3

class DatabaseManager:
    def __init__(self, db_name):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()

    def create_customer_table(self):
        try:
            self.cursor.execute("DROP TABLE IF EXISTS customers")
            self.cursor.execute("""CREATE TABLE IF NOT EXISTS customers (
                        customer_id TEXT PRIMARY KEY, 
                        first_name TEXT NOT NULL, 
                        last_name TEXT NOT NULL,
                        username TEXT NOT NULL,
                        password TEXT NOT NULL, 
                        email TEXT NOT NULL, 
                        phone_number TEXT NOT NULL, 
                        address TEXT, 
                        bio TEXT)""")
            self.conn.commit()
            print("Table 'customers' created successfully")
        except Exception as e:
            print(f"Error creating table: {str(e)}")

    def create_profile(self, customer_data):
        try:
            self.cursor.execute("""INSERT INTO customers (customer_id, first_name, last_name, username, password, email, phone_number, address, bio)
                                   VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)""", customer_data)
            self.conn.commit()
            print("Profile created successfully")
        except Exception as e:
            print(f"Error creating profile: {str(e)}")

    def fetch_data(self):
        try:
            self.cursor.execute("SELECT * FROM customers")
            return self.cursor.fetchall()
        except Exception as e:
            print(f"Error fetching data: {str(e)}")
            return []

    def update_data(self, customer_id, updated_data):
        try:
            self.cursor.execute("""UPDATE customers SET 
                                   first_name=?, last_name=?, username=?, password=?, email=?, phone_number=?, address=?, bio=? 
                                   WHERE customer_id=?""", updated_data + (customer_id,))
            self.conn.commit()
            print("Profile updated successfully")
        except Exception as e:
            print(f"Error updating profile: {str(e)}")

    
    def update_partial_data(self, customer_id, new_data):
       
        filtered_data = {k: v for k, v in new_data.items() if v}
        updates = ", ".join(f"{key} = ?" for key in filtered_data.keys())
        sql = f"UPDATE customers SET {updates} WHERE customer_id = ?"

        params = list(filtered_data.values()) + [customer_id]

        try:
            self.cursor.execute(sql, params)
            self.conn.commit()
        except Exception as e:
            print(f"Error updating data: {e}")
            raise

    def delete_data(self, customer_id):
        try:
            self.cursor.execute("DELETE FROM customers WHERE customer_id=?", (customer_id,))
            self.conn.commit()
            print("Profile deleted successfully")
        except Exception as e:
            print(f"Error deleting profile: {str(e)}")