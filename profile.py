import tkinter as tk
import db

class ProfileWindow:
    def __init__(self, username):
        self.win = tk.Toplevel()
        self.win.title("Profile")
        conn = db.get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT name FROM users WHERE username=%s", (username,))
        name = cursor.fetchone()[0]
        cursor.close()
        conn.close()
        tk.Label(self.win, text=f"Username: {username}").pack()
        tk.Label(self.win, text=f"Name: {name}").pack()
        tk.Button(self.win, text="Close", command=self.win.destroy).pack()
