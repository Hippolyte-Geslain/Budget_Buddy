def deposit(self, account_id, amount):   
    """Dépose une somme sur le compte."""
    amount = float(amount)
    if amount <= 0:
        return "Le montant doit être positif."

    try:
        sql = "UPDATE accounts SET deposits = deposits + %s, balance = balance + %s WHERE id = %s"
        self.cursor.execute(sql, (amount, amount, account_id))
        self.conn.commit()
        logging.info(f"Dépôt de {amount}€ sur le compte {account_id}.")
        return f"Dépôt de {amount}€ effectué avec succès."
    except Exception as e:
        self.conn.rollback()
        logging.error(f"Erreur lors du dépôt : {e}")
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
        sql = "UPDATE accounts SET debits = debits + %s, balance = balance - %s WHERE id = %s"
        self.cursor.execute(sql, (amount, amount, account_id))
        self.conn.commit()
        logging.info(f"Retrait de {amount}€ du compte {account_id}.")
        return f"Retrait de {amount}€ effectué avec succès."
    except Exception as e:
        self.conn.rollback()
        logging.error(f"Erreur lors du retrait : {e}")
        return f"Erreur : {e}"