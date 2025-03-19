from users import Users
from connect import connect_db

class Accounts:
    def __init__(self):
        self.conn = connect_db()
        self.cursor = self.conn.cursor()
        self.user = Users()
        
    def create_account(self, user_id, account_name, debits=0, deposits=0):
        balance = deposits - debits 
        sql = """
            INSERT INTO accounts (id_users, account_name, debits, deposits, balance) 
            VALUES (%s, %s, %s, %s, %s)
        """
        self.cursor.execute(sql, (user_id, account_name, debits, deposits, balance))
        self.conn.commit()

    def get_balance(self, account_id):
        sql = "SELECT balance FROM accounts WHERE id = %s"
        self.cursor.execute(sql, (account_id,))
        result = self.cursor.fetchone()
        return result[0] if result else None

    def deposit(self, account_id, amount):
        if amount <= 0:
            print("Le montant doit être positif.")
            return False
        
        sql = """
            UPDATE accounts 
            SET deposits = deposits + %s, balance = balance + %s 
            WHERE id = %s
        """
        self.cursor.execute(sql, (amount, amount, account_id))
        self.conn.commit()
        print(f"Déposé {amount} sur le compte {account_id}.")
        return True

    def withdraw(self, account_id, amount):
        balance = self.get_balance(account_id)
        
        if balance is None:
            print("Compte introuvable.")
            return False

        if amount <= 0:
            print("Le montant doit être positif.")
            return False

        if balance < amount:
            print("Fonds insuffisants.")
            return False

        sql = """
            UPDATE accounts 
            SET debits = debits + %s, balance = balance - %s 
            WHERE id = %s
        """
        self.cursor.execute(sql, (amount, amount, account_id))
        self.conn.commit()
        print(f"Retiré {amount} du compte {account_id}.")
        return True

    def transfer(self, from_account, to_account, amount):
        if amount <= 0:
            print("Le montant doit être positif.")
            return False

        balance = self.get_balance(from_account)
        if balance is None or balance < amount:
            print("Fonds insuffisants ou compte introuvable.")
            return False

        # Débiter le compte source
        if not self.withdraw(from_account, amount):
            return False

        # Créditer le compte destinataire
        if not self.deposit(to_account, amount):
            return False

        # Insérer le transfert dans la table `transfers`
        sql = """
            INSERT INTO transfers (from_account, to_account, amount) 
            VALUES (%s, %s, %s)
        """
        self.cursor.execute(sql, (from_account, to_account, amount))
        self.conn.commit()
        print(f"Transféré {amount} de {from_account} vers {to_account}.")
        return True

    def get_transactions(self, account_id):
        sql = """
            SELECT id, description, amount, date, type, categories 
            FROM transaction 
            WHERE id_accounts = %s 
            ORDER BY date DESC
        """
        self.cursor.execute(sql, (account_id,))
        return self.cursor.fetchall()

    def get_transfers(self, account_id):
        sql = """
            SELECT * FROM transfers 
            WHERE from_account = %s OR to_account = %s
            ORDER BY id DESC
        """
        self.cursor.execute(sql, (account_id, account_id))
        return self.cursor.fetchall()
