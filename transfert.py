import tkinter as tk
from tkinter import ttk

root = tk.Tk()

root.title("Page de Transfert d'Argent")

root.geometry("1200x700")

root.grid_columnconfigure(0, weight=1)  # Make column 0 expandable
root.grid_columnconfigure(1, weight=1)  # Make column 1 expandable
root.grid_columnconfigure(2, weight=1)  # Make column 2 expandable
root.grid_columnconfigure(3, weight=1)  # Make column 3 expandable
root.grid_columnconfigure(4, weight=1)  # Make column 4 expandable

# Labels
header = tk.Label(root, text="Transfert d'Argent vers un Compte", font=("Arial", 16))
header.grid(row=0, column=2, pady=20, sticky="n")

# Textbox to display transfer history
transfer_history_text = tk.Text(root, height=10, width=100)
transfer_history_text.grid(row=1, column=1, columnspan=3, padx=10, pady=10)

# Categories and corresponding actions (for history)
transfer_history_data = []

# Function to add a transfer entry to the history
def add_to_transfer_history(entry):
    transfer_history_text.insert(tk.END, entry + "\n")
    transfer_history_text.yview(tk.END)  # Scroll to the bottom to show the latest entry

# Function to perform a transfer
def perform_transfer():
    amount = amount_entry.get()
    account_type = account_type_combobox.get()
    account_id = account_id_entry.get()

    if amount and account_type and account_id:
        transfer_details = f"Transfert de {amount}€ vers un compte {account_type} ({account_id})"
        transfer_history_data.append(transfer_details)
        add_to_transfer_history(transfer_details)
        print(f"Transfert effectué : {transfer_details}")
    else:
        print("Veuillez remplir tous les champs.")
        
# Function to clear transfer history
def clear_transfer_history():
    transfer_history_text.delete(1.0, tk.END)

# Fields for transfer details
amount_label = tk.Label(root, text="Montant à transférer")
amount_label.grid(row=2, column=1, pady=10, sticky="w")

amount_entry = tk.Entry(root)
amount_entry.grid(row=2, column=2, padx=10, pady=10, sticky="ew")

# Combobox for selecting account type
account_type_label = tk.Label(root, text="Type de compte")
account_type_label.grid(row=3, column=1, pady=10, sticky="w")

account_type_combobox = ttk.Combobox(root, values=["Interne", "Externe"])
account_type_combobox.grid(row=3, column=2, pady=10, padx=10)
account_type_combobox.set("Interne")  # Set default value

# Field for entering account ID
account_id_label = tk.Label(root, text="ID du compte")
account_id_label.grid(row=4, column=1, pady=10, sticky="w")

account_id_entry = tk.Entry(root)
account_id_entry.grid(row=4, column=2, padx=10, pady=10, sticky="ew")

# Buttons
transfer_button = tk.Button(root, text="Effectuer le Transfert", command=perform_transfer)
transfer_button.grid(row=5, column=1, columnspan=2, pady=10)

clear_button = tk.Button(root, text="Effacer l'historique des transferts", command=clear_transfer_history)
clear_button.grid(row=6, column=1, columnspan=3, pady=10)

root.mainloop()

