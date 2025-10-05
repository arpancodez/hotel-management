# dashboard.py
import tkinter as tk
from rooms import RoomsWindow
from reservations import ReservationsWindow

class DashboardWindow:
    def __init__(self, master, username):
        self.master = master
        self.master.title("Dashboard")
        # Profile, Logout buttons
        # Display room count, sales, etc.
        tk.Button(master, text="Rooms", command=self.open_rooms).pack()
        tk.Button(master, text="Reservations", command=self.open_reservations).pack()
    
    def open_rooms(self):
        RoomsWindow()
    def open_reservations(self):
        ReservationsWindow()
