import tkinter as tk

root = tk.Tk()

root.title("Historique des Actions")

root.geometry("1200x700")

root.grid_columnconfigure(0, weight=1)  # Make column 0 expandable
root.grid_columnconfigure(1, weight=1)  # Make column 1 expandable
root.grid_columnconfigure(2, weight=1)  # Make column 2 expandable
root.grid_columnconfigure(3, weight=1)  # Make column 3 expandable
root.grid_columnconfigure(4, weight=1)  # Make column 4 expandable

# Labels
header = tk.Label(root, text="Historique des Actions Récentes", font=("Arial", 16))
header.grid(row=0, column=2, pady=20, sticky="n")

# Textbox to display history
history_text = tk.Text(root, height=20, width=100)
history_text.grid(row=1, column=1, columnspan=3, padx=10, pady=10)

# Example of adding a history entry
def add_to_history(entry):
    history_text.insert(tk.END, entry + "\n")
    history_text.yview(tk.END)  # Scroll to the bottom to show the latest entry

# Buttons for adding history entries
button1 = tk.Button(root, text="Ajouter une action", command=lambda: add_to_history("Action 1 effectuée"))
button1.grid(row=2, column=1, pady=10, padx=10)

button2 = tk.Button(root, text="Ajouter une autre action", command=lambda: add_to_history("Action 2 effectuée"))
button2.grid(row=2, column=2, pady=10, padx=10)

button3 = tk.Button(root, text="Effacer l'historique", command=lambda: history_text.delete(1.0, tk.END))
button3.grid(row=2, column=3, pady=10, padx=10)

root.mainloop()
