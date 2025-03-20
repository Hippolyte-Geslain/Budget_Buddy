import tkinter as tk

root = tk.Tk()

root.title("Bunny Budget")

root.geometry("1200x700")

root.grid_columnconfigure(0, weight=1)  # Make column 0 expandable
root.grid_columnconfigure(1, weight=1)  # Make column 1 expandable
root.grid_columnconfigure(2, weight=1)  # Make column 2 expandable
root.grid_columnconfigure(3, weight=1)  # Make column 3 expandable
root.grid_columnconfigure(4, weight=1)  # Make column 4 expandable

#Labels

header = tk.Label(root, text="Bienvenue sur votre espace personnel\nVous avez une vue d'ensemble ici !")
header.grid(row=0, column=1, pady=20, sticky="n")

dernieresDepenses = tk.Text(root,height=15, width=50)
dernieresDepenses.grid(row=1, column=1, pady=20, sticky="n")
dernieresDepenses.insert("1.0","Comptes + diagramme")

nom = tk.Label(root, text="Nom")
nom.grid(row=2, column=1, pady=20, sticky="n")

email = tk.Label(root, text="Email")
email.grid(row=3, column=1, pady=20, sticky="n")

mdp = tk.Label(root, text="Mot de passe")
mdp.grid(row=4, column=1, pady=20, sticky="n")

#Entries

entry1 = tk.Entry(root)
entry2 = tk.Entry(root)
entry3 = tk.Entry(root)
entry4 = tk.Entry(root)

entry1.grid(row=1, column=2, padx=10, pady=10, sticky="ew")  # Center horizontally
entry2.grid(row=2, column=2, padx=10, pady=10, sticky="ew")  # Center horizontally
entry3.grid(row=3, column=2, padx=10, pady=10, sticky="ew")  # Center horizontally
entry4.grid(row=4, column=2, padx=10, pady=10, sticky="ew")  # Center horizontally

#buttons

button1 = tk.Button(root, text="Connexion")
button1.grid(row=5, column=2, pady=10)

def on_click(event=None):
    prenom = entry1.get()
    nom = entry2.get()
    email = entry3.get()
    mdp = entry4.get()
    print(f"Prénom: {prenom}\nNom: {nom}\nEmail: {email}\nMot de passe: {mdp}")

button1.config(command=on_click)

root.bind('<Return>', on_click)

root.mainloop()