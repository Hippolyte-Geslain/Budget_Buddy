import tkinter as tk
from gui import Application

def main():
    root = tk.Tk()
    root.title("Budget Buddy")
    app = Application(root)
    root.mainloop()

if __name__ == "__main__":
    main()