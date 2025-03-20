from email.mime import message
import tkinter as tk
from tkinter import messagebox

root = tk.Tk()

root.title("Budget Bunny")

root.geometry("1200x700")

root.grid_columnconfigure(0, weight=1)  # Make column 0 expandable
root.grid_columnconfigure(1, weight=1)  # Make column 1 expandable
root.grid_columnconfigure(2, weight=1)  # Make column 2 expandable
root.grid_columnconfigure(3, weight=1)  # Make column 3 expandable
root.grid_columnconfigure(4, weight=1)  # Make column 4 expandable

header = tk.Label(root, text="Bienvenue à Budget Bunny!")
header.grid(row=0, column=2, pady=20, sticky="n")

email= tk.Label(root, text="Email")
email.grid(row=1, column=1, pady=20, sticky="n")

mdp=tk.Label(root, text="Mot de passe")
mdp.grid(row=2, column=1, pady=20, sticky="n")

entry1 = tk.Entry(root)
entry2 = tk.Entry(root)

entry1.grid(row=1, column=2, padx=10, pady=10, sticky="ew")  # Center horizontally
entry2.grid(row=2, column=2, padx=10, pady=10, sticky="ew")  # Center horizontally

button1 = tk.Button(root, text="Connexion")
button1.grid(row=3, column=2, pady=10)

def check_entries(email):
    if not "@" in email:
        return False
    else:
        return True

def on_click(event=None):
    username = entry1.get()
    password = entry2.get()
    if check_entries(username):
        values=[username,password]
        if not all(values):
            messagebox.showwarning("Attention", "Veuillez remplir tous les champs.")
        else:
            messagebox.showinfo("Succès","Connexion à votre compte en cours...")
        print(f"utilisateur = {username}\nmot de passe = {password}")
    else:
        messagebox.showwarning("Attention", "Veuillez utilisez une adresse mail valide")

button1.config(command=on_click)

root.bind('<Return>', on_click)

root.mainloop()