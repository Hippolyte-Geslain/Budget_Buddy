import mysql.connector
import bcrypt
class Database:
    def __init__(self):
        self.connection = mysql.connector.connect(
            host="localhost",
            user="root",  
            password="123",  
            database="budget_bunny"
        )
        self.cursor = self.connection.cursor()

    def create_user(self, name, surname, email, password):
        """Insert a new user into the users table."""
        try:
            hashed_password = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
            query = """
            INSERT INTO users (name, surname, email, password_hash)
            VALUES (%s, %s, %s, %s)
            """
            self.cursor.execute(query, (name, surname, email, hashed_password))
            self.connection.commit()  # Save changes to the database
        except Exception as e:
            self.connection.rollback()  # Rollback in case of an error
            raise e

    def execute_query(self, query, params=None):
        self.cursor.execute(query, params)
        self.connection.commit()

    def fetch_all(self, query, params=None):
        self.cursor.execute(query, params)
        return self.cursor.fetchall()

    def fetch_one(self, query, params=None):
        self.cursor.execute(query, params)
        return self.cursor.fetchone()
    
    def verify_user(self, email, password):
        """Vérifie si l'utilisateur existe et si le mot de passe est correct."""
        query = "SELECT * FROM users WHERE email = %s"
        self.cursor.execute(query, (email,))
        user = self.cursor.fetchone()

        if user and self.check_password(password, user[4]):
            return user  # Retourne les infos de l'utilisateur si le mot de passe est valide
        return None

    def check_password(self, input_password, stored_password):
        """Vérifie si le mot de passe hashé correspond."""
        return bcrypt.checkpw(input_password.encode(), stored_password.encode())