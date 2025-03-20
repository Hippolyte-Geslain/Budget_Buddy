import tkinter as tk

root = tk.Tk()

root.title("Bunny Paraùètres")

root.geometry("1200x700")

root.grid_columnconfigure(0, weight=1)  # Make column 0 expandable
root.grid_columnconfigure(1, weight=1)  # Make column 1 expandable
root.grid_columnconfigure(2, weight=1)  # Make column 2 expandable
root.grid_columnconfigure(3, weight=1)  # Make column 3 expandable
root.grid_columnconfigure(4, weight=1)  # Make column 4 expandable

#Labels

header = tk.Label(root, text="Pour changer vos informations personnelles\nEntrez votre mot de passe actuel")
header.grid(row=0, column=2, pady=20, sticky="n")

mdp = tk.Label(root, text="Mot de passe")
mdp.grid(row=1, column=1, pady=20, sticky="n")

mdp2 = tk.Label(root, text="Confirmez votre mot de passe")
mdp2.grid(row=2, column=1, pady=20, sticky="n")

#Entries

entry1 = tk.Entry(root)
entry2 = tk.Entry(root)

entry1.grid(row=1, column=2, padx=10, pady=10, sticky="ew")  # Center horizontally
entry2.grid(row=2, column=2, padx=10, pady=10, sticky="ew")  # Center horizontally

#buttons

button1 = tk.Button(root, text="Connexion")
button1.grid(row=5, column=2, pady=10)

def on_click(event=None):
    mdp = entry1.get()
    mdp2 = entry2.get()
    print(f"mdp1: {mdp}\nmdp2: {mdp2}")

button1.config(command=on_click)

root.bind('<Return>', on_click)

root.mainloop()