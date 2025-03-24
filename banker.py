import tkinter as tk
from tkinter import messagebox

# Simuler une base de données d'utilisateurs avec des informations de compte
users = {
    "user1": {"name": "Alice", "balance": 1000},
    "user2": {"name": "Bob", "balance": 1500},
    "user3": {"name": "Charlie", "balance": 2000}
}

# Fonction pour afficher les informations d'un utilisateur
def show_user_info(username):
    if username in users:
        user = users[username]
        info_label.config(text=f"Nom: {user['name']}\nSolde: {user['balance']}€")
    else:
        info_label.config(text="Utilisateur non trouvé")

# Fonction pour modifier le solde d'un utilisateur
def modify_balance(username, amount):
    if username in users:
        users[username]['balance'] += amount
        show_user_info(username)  # Met à jour l'affichage
        messagebox.showinfo("Succès", f"Solde de {username} mis à jour avec succès.")
    else:
        messagebox.showerror("Erreur", "Utilisateur non trouvé.")

# Fonction pour verrouiller un compte (simulé)
def lock_account(username):
    if username in users:
        messagebox.showinfo("Compte verrouillé", f"Le compte de {username} a été verrouillé.")
        # Ici, vous pouvez ajouter plus de logique pour simuler un verrouillage
    else:
        messagebox.showerror("Erreur", "Utilisateur non trouvé.")

# Fonction pour fermer la fenêtre
def close_window():
    root.quit()

# Créer la fenêtre principale
root = tk.Tk()
root.title("Fenêtre du Banquier")
root.geometry("500x400")

# Ajouter un titre
title_label = tk.Label(root, text="Bienvenue Banquier", font=("Arial", 18))
title_label.pack(pady=10)

# Liste des utilisateurs
user_list_label = tk.Label(root, text="Sélectionner un utilisateur:", font=("Arial", 12))
user_list_label.pack(pady=10)

# Liste déroulante des utilisateurs
usernames = list(users.keys())
selected_user = tk.StringVar()
selected_user.set(usernames[0])  # Par défaut, sélectionner le premier utilisateur
user_menu = tk.OptionMenu(root, selected_user, *usernames)
user_menu.pack(pady=10)

# Afficher les informations de l'utilisateur sélectionné
info_label = tk.Label(root, text="Informations de l'utilisateur", font=("Arial", 12))
info_label.pack(pady=10)

# Ajouter des boutons pour effectuer des actions sur les comptes
modify_button = tk.Button(root, text="Modifier Solde", font=("Arial", 12), 
                          command=lambda: modify_balance(selected_user.get(), 500))  # Ajouter 500€ par exemple
modify_button.pack(pady=10)

lock_button = tk.Button(root, text="Verrouiller Compte", font=("Arial", 12), 
                        command=lambda: lock_account(selected_user.get()))
lock_button.pack(pady=10)

# Fermer la fenêtre
close_button = tk.Button(root, text="Fermer", font=("Arial", 12), command=close_window)
close_button.pack(pady=20)

# Lancer la fenêtre principale
root.mainloop()
