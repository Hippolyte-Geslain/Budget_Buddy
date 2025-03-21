import tkinter as tk
from tkinter import ttk
from turtle import width
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt

root = tk.Tk()
root.title("Bunny Budget")
root.geometry("1200x700")

# Configure grid layout
for i in range(5):
    root.grid_columnconfigure(i, weight=1)
for i in range(10):
    root.grid_rowconfigure(i, weight=1)

# Header
header = tk.Label(root, text="Bienvenue sur votre espace personnel\nVous avez une vue d'ensemble ici !", font=("Arial", 16))
header.grid(row=0, column=0, columnspan=5, pady=20, sticky="n")

# Résumé des comptes
accounts_label = tk.Label(root, text="Résumé des comptes", font=("Arial", 14))
accounts_label.grid(row=1, column=0, pady=10, sticky="w")

accounts_list = tk.Listbox(root, height=5,width=5)
accounts_list.insert(1, "Compte courant : 1500€")
accounts_list.insert(2, "Livret A : 3000€")
accounts_list.insert(3, "PEL : 5000€")
accounts_list.grid(row=2, column=0,padx=20, pady=10, sticky="nsew")

# Dernières transactions
transactions_label = tk.Label(root, text="Dernières transactions", font=("Arial", 14),width=20)
transactions_label.grid(row=1, column=1, pady=10, sticky="w")

transactions_tree = ttk.Treeview(root, columns=("Date", "Description", "Montant"), show="headings", height=5)
transactions_tree.heading("Date", text="Date")
transactions_tree.column("Date",width=70)

transactions_tree.heading("Description", text="Description")
transactions_tree.column("Description",width=150)

transactions_tree.heading("Montant", text="Montant")
transactions_tree.column("Montant",width=55)

transactions_tree.insert("", "end", values=("21/03/2025", "Achat supermarché", "-50€"))
transactions_tree.insert("", "end", values=("20/03/2025", "Virement salaire", "+2000€"))
transactions_tree.grid(row=2, column=1, padx=20, pady=10, sticky="nsew")

# Graphique circulaire (répartition des dépenses)
fig, ax = plt.subplots()
categories = ['Logement', 'Alimentation', 'Loisirs', 'Transport']
values = [500, 300, 200, 100]
ax.pie(values, labels=categories, autopct='%1.1f%%', startangle=90)
ax.set_title("Répartition des dépenses")

canvas = FigureCanvasTkAgg(fig, master=root)
canvas.draw()
canvas.get_tk_widget().grid(row=2, column=2, padx=20, pady=10, sticky="nsew")

# Barre de recherche
search_label = tk.Label(root, text="Rechercher une transaction :", font=("Arial", 12))
search_label.grid(row=3, column=0, pady=10, sticky="w")

search_entry = tk.Entry(root, width=30)
search_entry.grid(row=3, column=1, padx=10, pady=10, sticky="ew")

search_button = tk.Button(root, text="Rechercher")
search_button.grid(row=3, column=2, padx=10, pady=10, sticky="ew")

# Boutons d'action
add_transaction_button = tk.Button(root, text="Ajouter une transaction")
add_transaction_button.grid(row=4, column=0, padx=10, pady=10, sticky="ew")

transfer_button = tk.Button(root, text="Transférer de l'argent")
transfer_button.grid(row=4, column=1, padx=10, pady=10, sticky="ew")

details_button = tk.Button(root, text="Voir les détails du compte")
details_button.grid(row=4, column=2, padx=10, pady=10, sticky="ew")

# Menu de navigation
menu = tk.Menu(root)
root.config(menu=menu)

file_menu = tk.Menu(menu, tearoff=0)
file_menu.add_command(label="Accueil")
file_menu.add_command(label="Transactions")
file_menu.add_command(label="Paramètres")
file_menu.add_separator()
file_menu.add_command(label="Quitter", command=root.quit)
menu.add_cascade(label="Menu", menu=file_menu)

root.mainloop()