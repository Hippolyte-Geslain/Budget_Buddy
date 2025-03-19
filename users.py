from connect import connect_db
import bcrypt

class Users:
    def __init__(self):
        self.conn = connect_db()
        self.cursor = self.conn.cursor()

    def __del__(self):
        self.conn.close()

    def add_user(self, name, surname, email, password):
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
        sql = "INSERT INTO users (name, surname, email, password_hash) VALUES (%s, %s, %s, %s)"
        self.cursor.execute(sql, (name, surname, email, hashed_password))
        self.conn.commit()

    def get_users(self):
        sql = "SELECT * FROM users"
        self.cursor.execute(sql)
        return self.cursor.fetchall()

    def get_user(self, email):
        sql = "SELECT * FROM users WHERE email = %s"
        self.cursor.execute(sql, (email,))
        return self.cursor.fetchone()

    def update_user(self, email, new_password):
        hashed_password = bcrypt.hashpw(new_password.encode('utf-8'), bcrypt.gensalt())
        sql = "UPDATE users SET password_hash = %s WHERE email = %s"
        self.cursor.execute(sql, (hashed_password, email))
        self.conn.commit()

    def delete_user(self, email):
        sql = "DELETE FROM users WHERE email = %s"
        self.cursor.execute(sql, (email,))
        self.conn.commit()

    def check_user(self, email):
        return bool(self.get_user(email))

    def check_password(self, email, password):
        user = self.get_user(email)
        if user:
            stored_password = user[4].encode('utf-8')  
            return bcrypt.checkpw(password.encode('utf-8'), stored_password)
        else:
            print("User not found")
            return False

    def sign_in(self, email, password):
        if self.check_user(email):
            if self.check_password(email, password):
                print("User signed in")
                return True
            else:
                print("Incorrect password")
                return False
        else:
            print("User not found. Please sign up.")
            return False

    def sign_up(self, name, surname, email, password):
        if self.check_user(email):
            print("User already exists")
            return False
        else:
            self.add_user(name, surname, email, password)
            print("User added successfully")
            return self.sign_in(email, password)
