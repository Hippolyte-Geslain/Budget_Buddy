import tkinter as tk
from tkinter import messagebox, ttk
import mysql.connector
import csv


def connect_db():
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="MOT de passe",
            database="Budget_Buddy"
        )
        return conn
    except mysql.connector.Error as err:
        messagebox.showerror("Database Error", f"Error: {err}")
        return None

