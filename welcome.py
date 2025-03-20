import tkinter as tk

# Fonction pour ouvrir la fenêtre de connexion
def open_login_window():
    login_window = tk.Toplevel(root)  # Fenêtre secondaire pour la connexion
    login_window.title("Connexion - Budget Buddy")
    login_window.geometry("400x300")

    # Label pour le titre de la connexion
    login_label = tk.Label(login_window, text="Veuillez entrer vos informations de connexion", font=("Arial", 14))
    login_label.grid(row=0, column=0, columnspan=2, pady=20)

    # Labels et champs de saisie pour l'email et le mot de passe
    email_label = tk.Label(login_window, text="Email")
    email_label.grid(row=1, column=0, pady=10, sticky="w")

    email_entry = tk.Entry(login_window)
    email_entry.grid(row=1, column=1, padx=10, pady=10, sticky="ew")

    password_label = tk.Label(login_window, text="Mot de passe")
    password_label.grid(row=2, column=0, pady=10, sticky="w")

    password_entry = tk.Entry(login_window, show="*")
    password_entry.grid(row=2, column=1, padx=10, pady=10, sticky="ew")

    # Bouton de connexion
    login_button = tk.Button(login_window, text="Se connecter", command=lambda: print(f"Connexion de {email_entry.get()}"))
    login_button.grid(row=3, column=0, columnspan=2, pady=20)

# Fonction pour ouvrir la fenêtre d'inscription
def open_register_window():
    register_window = tk.Toplevel(root)  # Fenêtre secondaire pour l'inscription
    register_window.title("Inscription - Budget Buddy")
    register_window.geometry("400x300")

    # Label pour le titre de l'inscription
    register_label = tk.Label(register_window, text="Veuillez entrer vos informations d'inscription", font=("Arial", 14))
    register_label.grid(row=0, column=0, columnspan=2, pady=20)

    # Labels et champs de saisie pour le nom, l'email et le mot de passe
    name_label = tk.Label(register_window, text="Nom")
    name_label.grid(row=1, column=0, pady=10, sticky="w")

    name_entry = tk.Entry(register_window)
    name_entry.grid(row=1, column=1, padx=10, pady=10, sticky="ew")

    email_label = tk.Label(register_window, text="Email")
    email_label.grid(row=2, column=0, pady=10, sticky="w")

    email_entry = tk.Entry(register_window)
    email_entry.grid(row=2, column=1, padx=10, pady=10, sticky="ew")

    password_label = tk.Label(register_window, text="Mot de passe")
    password_label.grid(row=3, column=0, pady=10, sticky="w")

    password_entry = tk.Entry(register_window, show="*")
    password_entry.grid(row=3, column=1, padx=10, pady=10, sticky="ew")

    # Bouton d'inscription
    register_button = tk.Button(register_window, text="S'inscrire", command=lambda: print(f"Inscription de {name_entry.get()}"))
    register_button.grid(row=4, column=0, columnspan=2, pady=20)

# Créer la fenêtre principale
root = tk.Tk()
root.title("Budget Buddy - Page d'Accueil")
root.geometry("600x400")

# Titre de l'application
app_title = tk.Label(root, text="Bienvenue sur Budget Buddy", font=("Arial", 24), pady=20)
app_title.pack()

# Description de l'application
description = tk.Label(root, text="L'application pour gérer vos finances personnelles", font=("Arial", 12))
description.pack(pady=10)

# Bouton pour s'identifier
login_button = tk.Button(root, text="S'identifier", font=("Arial", 14), command=open_login_window)
login_button.pack(pady=20)

# Bouton pour s'inscrire
register_button = tk.Button(root, text="S'inscrire", font=("Arial", 14), command=open_register_window)
register_button.pack(pady=20)

# Lancer la fenêtre principale
root.mainloop()
