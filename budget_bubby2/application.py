class Application:
    def __init__(self, master):
        self.master = master
        self.controller = Controller()
        self.create_login_screen()

    def create_login_screen(self):
        self.clear_screen()
        self.master.title("Connexion")
        
        self.label_email = tk.Label(self.master, text="Email:")
        self.label_email.pack(pady=5)
        self.entry_email = tk.Entry(self.master)
        self.entry_email.pack(pady=5)
        
        self.label_password = tk.Label(self.master, text="Mot de passe:")
        self.label_password.pack(pady=5)
        self.entry_password = tk.Entry(self.master, show="*")
        self.entry_password.pack(pady=5)
        
        self.btn_login = tk.Button(self.master, text="Se connecter", command=self.login)
        self.btn_login.pack(pady=10)
        
        self.btn_register = tk.Button(self.master, text="S'inscrire", command=self.create_register_screen)
        self.btn_register.pack(pady=10)

    def login(self):
        email = self.entry_email.get()
        password = self.entry_password.get()
        
        user = self.controller.login(email, password)
        if user:
            messagebox.showinfo("Connexion réussie", f"Bienvenue, {user.name}!")
            self.create_account_screen(user)  # Passer à l'écran de création de compte
        else:
            messagebox.showerror("Erreur", "Email ou mot de passe incorrect")

    def create_register_screen(self):
        self.clear_screen()
        self.master.title("Inscription")
        
        self.label_name = tk.Label(self.master, text="Nom:")
        self.label_name.pack(pady=5)
        self.entry_name = tk.Entry(self.master)
        self.entry_name.pack(pady=5)

        self.label_surname = tk.Label(self.master, text="Prénom:")
        self.label_surname.pack(pady=5)
        self.entry_surname = tk.Entry(self.master)
        self.entry_surname.pack(pady=5)

        self.label_email = tk.Label(self.master, text="Email:")
        self.label_email.pack(pady=5)
        self.entry_email = tk.Entry(self.master)
        self.entry_email.pack(pady=5)

        self.label_password = tk.Label(self.master, text="Mot de passe:")
        self.label_password.pack(pady=5)
        self.entry_password = tk.Entry(self.master, show="*")
        self.entry_password.pack(pady=5)

        self.btn_register = tk.Button(self.master, text="S'inscrire", command=self.register)
        self.btn_register.pack(pady=10)

    def register(self):
        name = self.entry_name.get()
        surname = self.entry_surname.get()
        email = self.entry_email.get()
        password = self.entry_password.get()

        user, message = self.controller.register(name, surname, email, password)
        if user:
            messagebox.showinfo("Inscription réussie", f"Bienvenue, {user.name}!")
            self.create_account_screen(user)  # Passer à l'écran de création de compte
        else:
            messagebox.showerror("Erreur", message)  # Affichage du message d'erreur

    def create_account_screen(self, user):
        """Création de l'écran pour ajouter un compte bancaire."""
        self.clear_screen()
        self.master.title("Créer un compte bancaire")
        
        self.label_account_name = tk.Label(self.master, text="Type de compte:")
        self.label_account_name.pack(pady=5)
        self.combo_account_name = tk.StringVar(self.master)
        self.combo_account_name.set("épargne")  # Valeur par défaut
        self.account_names = ["épargne", "joint", "entreprise"]
        self.drop_account_name = tk.OptionMenu(self.master, self.combo_account_name, *self.account_names)
        self.drop_account_name.pack(pady=5)

        self.btn_create_account = tk.Button(self.master, text="Créer le compte", command=lambda: self.create_account(user))
        self.btn_create_account.pack(pady=10)

    def create_account(self, user):
        account_name = self.combo_account_name.get()

        message = self.controller.create_account(user.id, account_name=account_name)
        if message == "Compte bancaire créé avec succès.":
            messagebox.showinfo("Succès", message)
            self.create_main_screen()  # Passer à l'écran principal
        else:
            messagebox.showerror("Erreur", message)  # Afficher une erreur si l'IBAN est déjà pris

    def create_main_screen(self):
        pass
