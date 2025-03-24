import tkinter as tk
from users import Users

# Initialisation de la gestion des utilisateurs
user_manager = Users()

# Fonction pour ouvrir la fenêtre de connexion
def open_login_window():
    login_window = tk.Toplevel(root)  
    login_window.title("Connexion - Budget Buddy")
    login_window.geometry("400x300")

    tk.Label(login_window, text="Veuillez entrer vos informations de connexion", font=("Arial", 14)).grid(row=0, column=0, columnspan=2, pady=20)

    tk.Label(login_window, text="Email").grid(row=1, column=0, pady=10, sticky="w")
    email_entry = tk.Entry(login_window)
    email_entry.grid(row=1, column=1, padx=10, pady=10, sticky="ew")

    tk.Label(login_window, text="Mot de passe").grid(row=2, column=0, pady=10, sticky="w")
    password_entry = tk.Entry(login_window, show="*")
    password_entry.grid(row=2, column=1, padx=10, pady=10, sticky="ew")

    def handle_login():
        email = email_entry.get()
        password = password_entry.get()
        if user_manager.sign_in(email, password):
            open_success_box("Connexion réussie", f"Bienvenue {email} !", login_window)
        else:
            open_success_box("Erreur", "Email ou mot de passe incorrect.", login_window)

    tk.Button(login_window, text="Se connecter", command=handle_login).grid(row=3, column=0, columnspan=2, pady=20)

# Fonction d'affichage de message
def open_success_box(title, message, window_to_close=None):
    success_window = tk.Toplevel(root)
    success_window.title(title)
    success_window.geometry("400x200")

    tk.Label(success_window, text=message, font=("Arial", 14)).pack(pady=20)
    tk.Button(success_window, text="OK", command=lambda: (success_window.destroy(), window_to_close.destroy() if window_to_close else None)).pack(pady=10)

# Fonction pour ouvrir la fenêtre d'inscription
def open_register_window():
    register_window = tk.Toplevel(root)  
    register_window.title("Inscription - Budget Buddy")
    register_window.geometry("400x350")

    tk.Label(register_window, text="Veuillez entrer vos informations d'inscription", font=("Arial", 14)).grid(row=0, column=0, columnspan=2, pady=20)

    tk.Label(register_window, text="Nom").grid(row=1, column=0, pady=10, sticky="w")
    name_entry = tk.Entry(register_window)
    name_entry.grid(row=1, column=1, padx=10, pady=10, sticky="ew")

    tk.Label(register_window, text="Prénom").grid(row=2, column=0, pady=10, sticky="w")
    surname_entry = tk.Entry(register_window)
    surname_entry.grid(row=2, column=1, padx=10, pady=10, sticky="ew")

    tk.Label(register_window, text="Email").grid(row=3, column=0, pady=10, sticky="w")
    email_entry = tk.Entry(register_window)
    email_entry.grid(row=3, column=1, padx=10, pady=10, sticky="ew")

    tk.Label(register_window, text="Mot de passe").grid(row=4, column=0, pady=10, sticky="w")
    password_entry = tk.Entry(register_window, show="*")
    password_entry.grid(row=4, column=1, padx=10, pady=10, sticky="ew")

    def handle_register():
        name = name_entry.get()
        surname = surname_entry.get()
        email = email_entry.get()
        password = password_entry.get()

        if user_manager.check_user(email):
            open_success_box("Erreur", f"L'utilisateur avec l'email {email} existe déjà.", register_window)
        else:
            success = user_manager.sign_up(name, surname, email, password)
            if success:
                open_success_box("Inscription réussie", f"Bienvenue {name} {surname} !", register_window)
                register_window.destroy()
            else:
                open_success_box("Erreur", "L'inscription a échoué. Vérifiez votre mot de passe il doit contenir au moins 8 lettre une majuscule un chiffre et un caractere spécial .", register_window)

    tk.Button(register_window, text="S'inscrire", command=handle_register).grid(row=5, column=0, columnspan=2, pady=20)

# Fenêtre principale
root = tk.Tk()
root.title("Budget Buddy - Page d'Accueil")
root.geometry("600x400")

tk.Label(root, text="Bienvenue sur Budget Buddy", font=("Arial", 24), pady=20).pack()
tk.Label(root, text="L'application pour gérer vos finances personnelles", font=("Arial", 12)).pack(pady=10)

tk.Button(root, text="S'identifier", font=("Arial", 14), command=open_login_window).pack(pady=20)
tk.Button(root, text="S'inscrire", font=("Arial", 14), command=open_register_window).pack(pady=20)

root.mainloop()