import tkinter as tk
from tkinter import messagebox, ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
from controllers import Controller

class Application:
    def __init__(self, master):
        self.master = master
        self.controller = Controller()
        self.create_login_screen()

    def create_login_screen(self):
        self.clear_screen()
        self.master.title("Connexion")
        
        tk.Label(self.master, text="Email:").pack(pady=5)
        self.entry_email = tk.Entry(self.master)
        self.entry_email.pack(pady=5)
        
        tk.Label(self.master, text="Mot de passe:").pack(pady=5)
        self.entry_password = tk.Entry(self.master, show="*")
        self.entry_password.pack(pady=5)
        
        tk.Button(self.master, text="Se connecter", command=self.login).pack(pady=10)
        tk.Button(self.master, text="S'inscrire", command=self.create_register_screen).pack(pady=10)

    def login(self):
        email = self.entry_email.get()
        password = self.entry_password.get()
        
        user = self.controller.login(email, password)
        if user:
            messagebox.showinfo("Connexion réussie", f"Bienvenue, {user.name}!")
            self.master.destroy()
            self.open_dashboard(user)
        else:
            messagebox.showerror("Erreur", "Email ou mot de passe incorrect")

    def create_register_screen(self):
        self.clear_screen()
        self.master.title("Inscription")
        
        tk.Label(self.master, text="Nom:").pack(pady=5)
        self.entry_name = tk.Entry(self.master)
        self.entry_name.pack(pady=5)

        tk.Label(self.master, text="Prénom:").pack(pady=5)
        self.entry_surname = tk.Entry(self.master)
        self.entry_surname.pack(pady=5)

        tk.Label(self.master, text="Email:").pack(pady=5)
        self.entry_email = tk.Entry(self.master)
        self.entry_email.pack(pady=5)

        tk.Label(self.master, text="Mot de passe:").pack(pady=5)
        self.entry_password = tk.Entry(self.master, show="*")
        self.entry_password.pack(pady=5)

        tk.Button(self.master, text="S'inscrire", command=self.register).pack(pady=10)

    def register(self):
        name = self.entry_name.get()
        surname = self.entry_surname.get()
        email = self.entry_email.get()
        password = self.entry_password.get()

        user, message = self.controller.register(name, surname, email, password)
        if user:
            messagebox.showinfo("Inscription réussie", f"Bienvenue, {user.name}!")
            self.master.destroy()
            self.open_dashboard(user)
        else:
            messagebox.showerror("Erreur", message)

    def open_dashboard(self, user):
        dashboard = tk.Tk()
        dashboard.title("Espace Personnel")
        dashboard.geometry("1200x700")

        tk.Label(dashboard, text=f"Bienvenue {user.name} !", font=("Arial", 16)).grid(row=0, column=0, columnspan=5, pady=20, sticky="n")

        tk.Label(dashboard, text="Résumé des comptes", font=("Arial", 14)).grid(row=1, column=0, pady=10, sticky="w")
        accounts_list = tk.Listbox(dashboard, height=5, width=40)
        
        tk.Button(dashboard, text="Transférer de l'argent", command=lambda: self.transfer_money_window(user)).grid(row=4, column=1, padx=10, pady=10, sticky="ew")

        
        accounts = self.controller.get_accounts(user.id)
        accounts_list.delete(0, tk.END)
    
        for account in accounts:
            accounts_list.insert(tk.END, f"{account.account_name} : {account.balance}€")
            accounts_list.grid(row=2, column=0,  padx=20, pady=10, sticky="nsew")
        
        tk.Label(dashboard, text="Dernières transactions", font=("Arial", 14)).grid(row=1, column=1, pady=10, sticky="w")
        transactions_tree = ttk.Treeview(dashboard, columns=("Date", "Description", "Montant"), show="headings", height=5)
        transactions_tree.heading("Date", text="Date")
        transactions_tree.heading("Description", text="Description")
        transactions_tree.heading("Montant", text="Montant")

        transactions = self.controller.get_transactions(user.id)
        for transaction in transactions:
            transactions_tree.insert("", "end", values=(transaction['date'], transaction['description'], f"{transaction['amount']}€"))
        
        transactions_tree.grid(row=2, column=1, padx=20, pady=10, sticky="nsew")
        
        tk.Button(dashboard, text="Ajouter une transaction", command=lambda: self.add_transaction(dashboard, user)).grid(row=4, column=0, padx=10, pady=10, sticky="ew")

        tk.Button(dashboard, text="Transférer de l'argent").grid(row=4, column=1, padx=10, pady=10, sticky="ew")

        tk.Button(dashboard, text="Voir les détails du compte").grid(row=4, column=2, padx=10, pady=10, sticky="ew")
        
        dashboard.mainloop()

    def add_transaction(self, parent, user):
        add_window = tk.Toplevel(parent)
        add_window.title("Ajouter une transaction")
    
        tk.Label(add_window, text="Description:").grid(row=0, column=0)
        desc_entry = tk.Entry(add_window)
        desc_entry.grid(row=0, column=1)
    
        tk.Label(add_window, text="Montant (€):").grid(row=1, column=0)
        amount_entry = tk.Entry(add_window)
        amount_entry.grid(row=1, column=1)

        # Charger les comptes de l'utilisateur
        accounts = self.controller.get_accounts(user.id)  # Passer l'ID de l'utilisateur pour récupérer ses comptes
        account_names = [account.account_name for account in accounts]
    
        if not account_names:
            messagebox.showerror("Erreur", "Aucun compte disponible.")
            add_window.destroy()
            return

        tk.Label(add_window, text="Compte:").grid(row=2, column=0)
        account_var = tk.StringVar(value=account_names[0])  # Valeur par défaut
        account_combobox = ttk.Combobox(add_window, textvariable=account_var, values=account_names)
        account_combobox.grid(row=2, column=1)
    
        tk.Label(add_window, text="Catégorie:").grid(row=3, column=0)
        category_options = ['salaire', 'loyer', 'alimentation', 'loisirs', 'autres']
        category_var = tk.StringVar(value='autres')  # Valeur par défaut
        category_combobox = ttk.Combobox(add_window, textvariable=category_var, values=category_options)
        category_combobox.grid(row=3, column=1)

        tk.Label(add_window, text="Type de transaction:").grid(row=4, column=0)
        transaction_type_var = tk.StringVar(value='deposit')  # Valeur par défaut
        transaction_type_combobox = ttk.Combobox(add_window, textvariable=transaction_type_var, values=['deposit', 'withdrawal'])
        transaction_type_combobox.grid(row=4, column=1)
    
        def submit():
            description = desc_entry.get()
            try:
                amount = float(amount_entry.get())
                transaction_type = transaction_type_var.get()  # Type de transaction sélectionné
                selected_account_name = account_var.get()  # Nom du compte sélectionné
            
                account_id = next(account.id for account in accounts if account.account_name == selected_account_name)

                category = category_var.get()
            
                message = self.controller.add_transaction(user.id, description, amount, account_id, transaction_type, category)
                messagebox.showinfo("Succès", message)
                add_window.destroy()
            except ValueError:
                messagebox.showerror("Erreur", "Veuillez entrer un montant valide.")
            except Exception as e:
                messagebox.showerror("Erreur", f"Erreur : {e}")

        tk.Button(add_window, text="Ajouter", command=submit).grid(row=4, column=0, columnspan=2)
        
    def transfer_money_window(self, user):
        transfer_window = tk.Toplevel()
        transfer_window.title("Effectuer un transfert")

        tk.Label(transfer_window, text="Montant (€):").grid(row=0, column=0)
        amount_entry = tk.Entry(transfer_window)
        amount_entry.grid(row=0, column=1)

        accounts = self.controller.get_accounts(user.id)
        account_names = [account.account_name for account in accounts]
    
        tk.Label(transfer_window, text="Compte source:").grid(row=1, column=0)
        from_account_var = tk.StringVar(value=account_names[0])
        from_account_combobox = ttk.Combobox(transfer_window, textvariable=from_account_var, values=account_names)
        from_account_combobox.grid(row=1, column=1)

        tk.Label(transfer_window, text="IBAN destinataire:").grid(row=2, column=0)
        iban_entry = tk.Entry(transfer_window)
        iban_entry.grid(row=2, column=1)

        def submit_transfer():
            try:
                amount = float(amount_entry.get())
                from_account_name = from_account_var.get()
                from_account_id = next(account.id for account in accounts if account.account_name == from_account_name)
                to_account_iban = iban_entry.get() or None
                message = self.controller.transfer_money(user.id, from_account_id, to_account_iban, amount)
                messagebox.showinfo("Transfert", message)
                transfer_window.destroy()
            except ValueError:
                messagebox.showerror("Erreur", "Veuillez entrer un montant valide.")
            except Exception as e:
                messagebox.showerror("Erreur", f"Erreur : {e}")

        tk.Button(transfer_window, text="Confirmer", command=submit_transfer).grid(row=3, column=0, columnspan=2)
        


    def clear_screen(self):
        for widget in self.master.winfo_children():
            widget.destroy()
