class User:
    def __init__(self, id, name, surname, email, password_hash):
        self.id = id
        self.name = name
        self.surname = surname
        self.email = email
        self.password_hash = password_hash

class Account:
    def __init__(self, id, account_name, iban, balance, user_id):
        self.id = id
        self.account_name = account_name
        self.iban = iban
        self.balance = balance
        self.user_id = user_id

class Transaction:
    def __init__(self, id, description, amount, transaction_date, transaction_type, account_id):
        self.id = id
        self.description = description
        self.amount = amount
        self.transaction_date = transaction_date
        self.transaction_type = transaction_type
        self.account_id = account_id
