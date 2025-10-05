# login.py
import tkinter as tk
from tkinter import messagebox
from dashboard import DashboardWindow
import db

class LoginWindow:
    def __init__(self, master):
        self.master = master
        self.master.title("Hotel Management Login")
        # Sign In form and Sign Up option code here...
        # On successful sign in:
        self.open_dashboard(username)

    def open_dashboard(self, username):
        self.master.destroy()
        new_root = tk.Tk()
        DashboardWindow(new_root, username)
        new_root.mainloop()
