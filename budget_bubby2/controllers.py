from database import Database
from models import Account, Transaction, User
import re
import logging
import random

class Controller:
    def __init__(self):
        self.db = Database()

    def get_balance(self,account_id):
        account_infos = self.db.fetch_one("SELECT * FROM accounts WHERE id = %s", (account_id))
        account_infos = float(account_infos[3])

    def deposit(self, account_id, amount):   
        """Dépose une somme sur le compte."""
        amount = float(amount)
        if amount <= 0:
            return "Le montant doit être positif."

        try:
            sql = "UPDATE accounts SET balance = balance + %s WHERE id = %s"
            self.db.execute_query(sql, (amount, account_id))
        except Exception as e:
            return f"Erreur : {e}"
        
    def withdraw(self, account_id, amount):
        """Effectue un retrait."""
        amount = float(amount)
        balance = self.get_balance(account_id)

        if balance is None:
            return "Compte introuvable."
        if amount <= 0:
            return "Le montant doit être positif."
        if balance < amount:
            return "Fonds insuffisants."

        try:
            sql = "UPDATE accounts SET balance = balance - %s WHERE id = %s"
            self.db.execute_query(sql, (amount, account_id))
        except Exception as e:
            return f"Erreur : {e}"

    def get_accounts(self, user_id):
        """Récupère les comptes d'un utilisateur spécifique."""
        query = "SELECT * FROM accounts WHERE id_users = %s"
        result = self.db.fetch_all(query, (user_id,))
        if not result:
            return []  # Liste vide si aucun compte n'est trouvé
        return [Account(*row) for row in result]

    def get_transactions(self, account_id):
        """Récupère les transactions d'un compte spécifique."""
        query = "SELECT * FROM transactions WHERE id_accounts = %s"
        result = self.db.fetch_all(query, (account_id,))
        if not result:
            return []  # Liste vide si aucune transaction n'est trouvée
        return [Transaction(*row) for row in result]

    def validate_password(self, password):
        """Valide les conditions du mot de passe."""
        if len(password) < 8:
            logging.error("Mot de passe trop court.")
            return False, "Le mot de passe doit contenir au moins 8 caractères."
        if not re.search(r'[A-Z]', password):
            logging.error("Mot de passe sans majuscule.")
            return False, "Le mot de passe doit contenir au moins une majuscule."
        if not re.search(r'[0-9]', password):
            logging.error("Mot de passe sans chiffre.")
            return False, "Le mot de passe doit contenir au moins un chiffre."
        if not re.search(r'[!@#$%^&*(),.?\":{}|<>]', password):
            logging.error("Mot de passe sans caractère spécial.")
            return False, "Le mot de passe doit contenir au moins un caractère spécial."
        return True, "Mot de passe valide."

    def login(self, email, password):
        """Vérifie les informations de connexion de l'utilisateur."""
        user = self.db.verify_user(email, password)
        return User(*user) if user else None

    def register(self, name, surname, email, password):
        """Enregistre un nouvel utilisateur."""
        is_valid, message = self.validate_password(password)
        if not is_valid:
            return None, message

        if self.db.fetch_one("SELECT * FROM users WHERE email = %s", (email,)):
            return None, "Un utilisateur avec cet email existe déjà."

        self.db.create_user(name, surname, email, password)
        return self.login(email, password), "Inscription réussie."

    def is_iban_unique(self, iban):
        """Vérifie si l'IBAN est unique dans la base de données."""
        self.db.cursor.execute("SELECT COUNT(*) FROM accounts WHERE iban = %s", (iban,))
        result = self.db.cursor.fetchone()  # Retourne un tuple
        return result[0] == 0  # Utiliser l'indice 0 pour récupérer le compte

    def calculate_rib_key(self, bank_code, branch_code, account_number):
        """Calcule la clé RIB."""
        rib_base = f"{bank_code}{branch_code}{account_number}"
        rib_number = int(rib_base) % 97
        rib_key = (97 - rib_number) % 97
        return f"{rib_key:02}"

    def calculate_iban_key(self, bban):
        """Calcule la clé IBAN."""
        iban_base = f"{bban}152700"
        iban_number = int(iban_base) % 97
        iban_key = (98 - iban_number) % 97
        return f"{iban_key:02}"

    def generate_french_iban(self):
        """Génère un IBAN français unique."""
        while True:
            bank_code = "30002"
            branch_code = "00550"
            account_number = "".join(str(random.randint(0, 9)) for _ in range(11))
            rib_key = self.calculate_rib_key(bank_code, branch_code, account_number)
            bban = f"{bank_code}{branch_code}{account_number}{rib_key}"
            iban_key = self.calculate_iban_key(bban)
            iban = f"FR{iban_key}{bban}"

            if self.is_iban_unique(iban):
                return iban

    def create_account(self, user_id, account_name, initial_deposit):
        """Crée un compte bancaire avec un dépôt initial obligatoire."""
        if initial_deposit < 20:
            return "Le dépôt initial doit être d'au moins 20€."
    
        iban = self.generate_french_iban()

        try:
            sql = """
            INSERT INTO accounts (id_users, account_name, balance, iban) 
            VALUES (%s, %s, %s, %s)
        """
            self.db.execute_query(sql, (user_id, account_name, initial_deposit, iban))
            return f"Compte '{account_name}' créé avec succès ! IBAN : {iban}"
        except Exception as e:
            return f"Erreur lors de la création du compte : {e}"

    def add_transaction(self, user_id, description, amount, account_id, transaction_type, category):
        """Ajoute une nouvelle transaction après validation des informations."""
        
        # Validation des données de la transaction
        if not description or len(description) == 0:
            return "La description ne peut pas être vide."
        
        if amount <= 0:
            return "Le montant doit être supérieur à zéro."

        if transaction_type not in ['deposit', 'withdrawal']:
            return "Le type de transaction est invalide."
        
        # Vérification de la validité de la catégorie
        valid_categories = ['salaire', 'loyer', 'alimentation', 'loisirs', 'autres']
        if category not in valid_categories:
            return "La catégorie sélectionnée est invalide."

        # Vérifier si le compte existe avant d'ajouter une transaction
        if not self.db.fetch_one("SELECT id FROM accounts WHERE id = %s AND id_users = %s", (account_id, user_id)):
            return "Le compte spécifié n'existe pas ou ne vous appartient pas."

        # Enregistrer la transaction dans la base de données
        try:
            # Récupérer l'ID de la catégorie à partir du nom de la catégorie
            category_id = self.get_category_id(category)
            
            sql = """
            INSERT INTO transactions (description, amount, type, id_accounts, id_category) 
            VALUES (%s, %s, %s, %s, %s)
            """
            self.db.execute_query(sql, (description, amount, transaction_type, account_id, category_id))
            logging.info(f"Transaction ajoutée : {description}, {amount}€, Type: {transaction_type}, Compte ID: {account_id}, Catégorie: {category}")
            return "Transaction ajoutée avec succès."
        
        except Exception as e:
            logging.error(f"Erreur lors de l'ajout de la transaction : {e}")
            return f"Erreur lors de l'ajout de la transaction : {e}"

    def get_category_id(self, category_name):
        """Retourne l'ID d'une catégorie en fonction de son nom."""
        query = "SELECT id FROM category WHERE category = %s"
        result = self.db.fetch_one(query, (category_name,))
        return result[0] if result else None
    
    def transfer_money(self, sender_user_id, from_account_id, to_account_iban, amount):
        try:
            # Ensure the amount is a valid float
            if amount <= 0:
                return "Le montant doit être supérieur à zéro."
        except ValueError:
            return "Le montant doit être un nombre valide."

        # Récupérer le compte de l'émetteur
        from_account = self.db.fetch_one("SELECT * FROM accounts WHERE id = %s AND id_users = %s", (from_account_id, sender_user_id))
        if not from_account:
            return "Compte émetteur introuvable."

        # Ensure from_balance is a float
        from_balance = float(from_account[3])  # Balance du compte émetteur

        # Vérification si le solde est suffisant
        if from_balance < amount:
            return "Solde insuffisant."

        # Vérification si l'IBAN du destinataire existe dans la base de données
        to_account = self.db.fetch_one("SELECT * FROM accounts WHERE iban = %s", (to_account_iban,))

        if to_account:
            # Transfert interne (vers un autre compte de la même plateforme)
            to_account_id = to_account[0]  # ID du destinataire
            new_from_balance = from_balance - amount
            new_to_balance = float(to_account[3]) + amount  # Ensure to_balance is a float

            try:
                # Mettre à jour les comptes de l'émetteur et du destinataire
                self.db.execute_query("UPDATE accounts SET balance = %s WHERE id = %s", (new_from_balance, from_account_id))
                self.db.execute_query("UPDATE accounts SET balance = %s WHERE id = %s", (new_to_balance, to_account_id))

                # Enregistrer la transaction dans la table transactions (transfert interne)
                self.add_transaction(sender_user_id, f"Transfert vers {to_account_id}", amount, from_account_id, 'withdrawal', 'autres')
                self.add_transaction(sender_user_id, f"Transfert depuis {from_account_id}", amount, to_account_id, 'deposit', 'autres')

                return "Transfert interne effectué avec succès."

            except Exception as e:
                return f"Erreur lors du transfert interne : {e}"

        else:
            # Transfert externe (vers un IBAN externe)
            new_from_balance = from_balance - amount

            try:
                # Mettre à jour le compte de l'émetteur
                self.db.execute_query("UPDATE accounts SET balance = %s WHERE id = %s", (new_from_balance, from_account_id))

                # Enregistrer la transaction dans la table transactions (transfert externe)
                self.add_transaction(sender_user_id, f"Transfert vers IBAN {to_account_iban}", amount, from_account_id, 'withdrawal', 'autres')

                return "Transfert externe effectué avec succès."

            except Exception as e:
                return f"Erreur lors du transfert externe : {e}"