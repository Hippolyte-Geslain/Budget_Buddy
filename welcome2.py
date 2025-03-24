import tkinter as tk
from PIL import Image, ImageTk  # Importation de Pillow pour gérer l'image

# Fonction pour ouvrir la fenêtre de connexion
def open_login_window():
    login_window = tk.Toplevel(root)  # Fenêtre secondaire pour la connexion
    login_window.title("Connexion - Budget Buddy")
    login_window.geometry("400x300")

    # Charger l'image de fond pour la fenêtre de connexion
    login_background_image = Image.open("image2.png")  # Remplace par le chemin de ton image
    login_background_image = login_background_image.resize((400, 300), Image.Resampling.LANCZOS)
    login_background_photo = ImageTk.PhotoImage(login_background_image)

    # Créer un canvas pour afficher l'image dans la fenêtre de connexion
    canvas_login = tk.Canvas(login_window, width=400, height=300)
    canvas_login.pack(fill="both", expand=True)

    # Ajouter l'image au canvas
    canvas_login.create_image(0, 0, anchor="nw", image=login_background_photo)

    # Garder une référence de l'image pour éviter qu'elle soit collectée par le garbage collector
    canvas_login.image = login_background_photo

    # Créer une frame pour contenir les champs et boutons au-dessus de l'image
    frame_login = tk.Frame(login_window, bg="white", bd=2)
    frame_login.place(relx=0.5, rely=0.5, anchor="center")

    # Label pour le titre de la connexion
    login_label = tk.Label(frame_login, text="Veuillez entrer vos informations de connexion", font=("Arial", 14))
    login_label.grid(row=0, column=0, columnspan=2, pady=20)

    # Labels et champs de saisie pour l'email et le mot de passe
    email_label = tk.Label(frame_login, text="Email")
    email_label.grid(row=1, column=0, pady=10, sticky="w")

    email_entry = tk.Entry(frame_login)
    email_entry.grid(row=1, column=1, padx=10, pady=10, sticky="ew")

    password_label = tk.Label(frame_login, text="Mot de passe")
    password_label.grid(row=2, column=0, pady=10, sticky="w")

    password_entry = tk.Entry(frame_login, show="*")
    password_entry.grid(row=2, column=1, padx=10, pady=10, sticky="ew")

    # Bouton de connexion
    login_button = tk.Button(frame_login, text="Se connecter", command=lambda: print(f"Connexion de {email_entry.get()}"))
    login_button.grid(row=3, column=0, columnspan=2, pady=20)

# Fonction pour ouvrir la fenêtre d'inscription
def open_register_window():
    register_window = tk.Toplevel(root)  # Fenêtre secondaire pour l'inscription
    register_window.title("Inscription - Budget Buddy")
    register_window.geometry("400x300")

    # Charger l'image de fond pour la fenêtre d'inscription
    register_background_image = Image.open("image2.png")  # Remplace par le chemin de ton image
    register_background_image = register_background_image.resize((400, 300), Image.Resampling.LANCZOS)
    register_background_photo = ImageTk.PhotoImage(register_background_image)

    # Créer un canvas pour afficher l'image dans la fenêtre d'inscription
    canvas_register = tk.Canvas(register_window, width=400, height=300)
    canvas_register.pack(fill="both", expand=True)

    # Ajouter l'image au canvas
    canvas_register.create_image(0, 0, anchor="nw", image=register_background_photo)

    # Garder une référence de l'image pour éviter qu'elle soit collectée par le garbage collector
    canvas_register.image = register_background_photo

    # Créer une frame pour contenir les champs et boutons au-dessus de l'image
    frame_register = tk.Frame(register_window, bg="white", bd=2)
    frame_register.place(relx=0.5, rely=0.5, anchor="center")

    # Label pour le titre de l'inscription
    register_label = tk.Label(frame_register, text="Veuillez entrer vos informations d'inscription", font=("Arial", 14))
    register_label.grid(row=0, column=0, columnspan=2, pady=20)

    # Labels et champs de saisie pour le nom, l'email et le mot de passe
    name_label = tk.Label(frame_register, text="Nom")
    name_label.grid(row=1, column=0, pady=10, sticky="w")

    name_entry = tk.Entry(frame_register)
    name_entry.grid(row=1, column=1, padx=10, pady=10, sticky="ew")

    email_label = tk.Label(frame_register, text="Email")
    email_label.grid(row=2, column=0, pady=10, sticky="w")

    email_entry = tk.Entry(frame_register)
    email_entry.grid(row=2, column=1, padx=10, pady=10, sticky="ew")

    password_label = tk.Label(frame_register, text="Mot de passe")
    password_label.grid(row=3, column=0, pady=10, sticky="w")

    password_entry = tk.Entry(frame_register, show="*")
    password_entry.grid(row=3, column=1, padx=10, pady=10, sticky="ew")

    # Bouton d'inscription
    register_button = tk.Button(frame_register, text="S'inscrire", command=lambda: print(f"Inscription de {name_entry.get()}"))
    register_button.grid(row=4, column=0, columnspan=2, pady=20)

# Créer la fenêtre principale
root = tk.Tk()
root.title("Budget Buddy - Page d'Accueil")
root.geometry("600x400")

# Charger l'image de fond pour la fenêtre principale
background_image = Image.open("image1.png")  # Remplace par le chemin de ton image
background_image = background_image.resize((600, 400), Image.Resampling.LANCZOS)
background_photo = ImageTk.PhotoImage(background_image)

# Créer un canvas pour afficher l'image de fond
canvas = tk.Canvas(root, width=600, height=400)
canvas.pack(fill="both", expand=True)

# Ajouter l'image au canvas
canvas.create_image(0, 0, anchor="nw", image=background_photo)

# Garder une référence de l'image pour éviter qu'elle soit collectée par le garbage collector
canvas.image = background_photo

# Créer une frame pour contenir les éléments au-dessus de l'image
frame = tk.Frame(root, bg="white", bd=2)
frame.place(relx=0.5, rely=0.5, anchor="center")

# Titre de l'application
app_title = tk.Label(frame, text="Bienvenue sur Budget Buddy", font=("Arial", 24), pady=20)
app_title.grid(row=0, column=0, columnspan=2)

# Description de l'application
description = tk.Label(frame, text="L'application pour gérer vos finances personnelles", font=("Arial", 12))
description.grid(row=1, column=0, columnspan=2, pady=10)

# Bouton pour s'identifier
login_button = tk.Button(frame, text="S'identifier", font=("Arial", 14), command=open_login_window)
login_button.grid(row=2, column=0, columnspan=2, pady=20)

# Bouton pour s'inscrire
register_button = tk.Button(frame, text="S'inscrire", font=("Arial", 14), command=open_register_window)
register_button.grid(row=3, column=0, columnspan=2, pady=20)

# Lancer la fenêtre principale
root.mainloop()

