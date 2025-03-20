import tkinter as tk
from tkinter import ttk

# Exemple d'historique de transferts
transfer_history_data = [
    "Transfert de 100€ vers un compte Interne (12345) | Catégorie: Alimentaire | Message: Achat de courses",
    "Transfert de 200€ vers un compte Externe (67890) | Catégorie: Divertissement | Message: Billet de concert"
]

# Fonction pour mettre à jour l'historique des transferts dans la fenêtre principale
def update_history_display():
    transfer_history_text.delete(1.0, tk.END)  # Efface l'historique actuel
    for transfer in transfer_history_data:
        transfer_history_text.insert(tk.END, transfer + "\n")
    transfer_history_text.yview(tk.END)  # Fait défiler jusqu'au bas pour afficher le dernier ajout

# Fonction pour modifier la catégorie d'une transaction
def modify_category(transaction_id, new_category):
    if transaction_id and new_category:
        # Trouver la transaction dans l'historique et mettre à jour sa catégorie
        found = False
        for idx, transfer in enumerate(transfer_history_data):
            if transaction_id in transfer:
                # Remplacer la vieille catégorie par la nouvelle
                updated_transfer = transfer.split(" | Catégorie: ")[0] + f" | Catégorie: {new_category}" + transfer.split(" | Catégorie: ")[1].split(" |")[1]
                transfer_history_data[idx] = updated_transfer
                found = True
                break

        if found:
            update_history_display()
            print(f"Transaction {transaction_id} mise à jour avec la catégorie {new_category}")
        else:
            print(f"Transaction avec l'ID {transaction_id} non trouvée.")
    else:
        print("Veuillez remplir tous les champs.")

# Créer la fenêtre principale
root = tk.Tk()
root.title("Historique des Transactions")
root.geometry("1200x700")

root.grid_columnconfigure(0, weight=1)  # Make column 0 expandable
root.grid_columnconfigure(1, weight=1)  # Make column 1 expandable
root.grid_columnconfigure(2, weight=1)  # Make column 2 expandable
root.grid_columnconfigure(3, weight=1)  # Make column 3 expandable
root.grid_columnconfigure(4, weight=1)  # Make column 4 expandable

# Label et texte pour afficher l'historique des transferts
header = tk.Label(root, text="Historique des Transferts", font=("Arial", 16))
header.grid(row=0, column=1, pady=20, sticky="n")

transfer_history_text = tk.Text(root, height=10, width=100)
transfer_history_text.grid(row=1, column=1, columnspan=3, padx=10, pady=10)

# Affichage initial de l'historique
update_history_display()

# Fonction pour ouvrir la fenêtre de modification de la catégorie
def open_modify_category_window():
    modify_window = tk.Toplevel(root)  # Fenêtre secondaire
    modify_window.title("Modifier la catégorie de la transaction")
    modify_window.geometry("500x300")

    # Label et champ de saisie pour l'ID de la transaction
    transaction_id_label = tk.Label(modify_window, text="ID de la transaction")
    transaction_id_label.grid(row=0, column=0, pady=10, sticky="w")

    transaction_id_entry = tk.Entry(modify_window)
    transaction_id_entry.grid(row=0, column=1, padx=10, pady=10, sticky="ew")

    # Label et champ de saisie pour la catégorie
    category_label = tk.Label(modify_window, text="Nouvelle catégorie")
    category_label.grid(row=1, column=0, pady=10, sticky="w")

    category_combobox = ttk.Combobox(modify_window, values=["Alimentaire", "Divertissement", "Services", "Autre"])
    category_combobox.grid(row=1, column=1, padx=10, pady=10, sticky="ew")
    category_combobox.set("Alimentaire")  # Valeur par défaut

    # Fonction de modification de la catégorie
    def modify():
        transaction_id = transaction_id_entry.get()
        new_category = category_combobox.get()
        modify_category(transaction_id, new_category)
        modify_window.destroy()  # Ferme la fenêtre après modification

    # Bouton pour modifier la catégorie
    modify_button = tk.Button(modify_window, text="Modifier la catégorie", command=modify)
    modify_button.grid(row=2, column=0, columnspan=2, pady=10)

# Bouton pour ouvrir la fenêtre de modification de la catégorie
modify_category_button = tk.Button(root, text="Modifier la catégorie d'une transaction", command=open_modify_category_window)
modify_category_button.grid(row=2, column=1, columnspan=3, pady=10)

# Lancer la fenêtre principale
root.mainloop()

