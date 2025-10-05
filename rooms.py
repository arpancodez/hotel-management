import tkinter as tk
import db

class RoomsWindow:
    def __init__(self):
        self.win = tk.Toplevel()
        self.win.title("Manage Rooms")
        tk.Button(self.win, text="Add Room", command=self.add_room).pack()
        tk.Button(self.win, text="View Rooms", command=self.view_rooms).pack()
        tk.Button(self.win, text="Update Room", command=self.update_room).pack()

    def add_room(self):
        win = tk.Toplevel(self.win)
        win.title("Add Room")
        tk.Label(win, text="Room Number:").pack()
        room_num_entry = tk.Entry(win)
        room_num_entry.pack()
        tk.Label(win, text="Room Type:").pack()
        type_entry = tk.Entry(win)
        type_entry.pack()
        tk.Label(win, text="Price:").pack()
        price_entry = tk.Entry(win)
        price_entry.pack()
        tk.Label(win, text="Status:").pack()
        status_entry = tk.Entry(win)
        status_entry.pack()
        tk.Button(win, text="Submit", command=lambda: self.save_room(room_num_entry.get(), type_entry.get(), price_entry.get(), status_entry.get(), win)).pack()

    def save_room(self, room_number, room_type, price, status, win):
        conn = db.get_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO rooms (room_number, room_type, price, status) VALUES (%s, %s, %s, %s)", (room_number, room_type, price, status))
        conn.commit()
        cursor.close()
        conn.close()
        win.destroy()

    def view_rooms(self):
        win = tk.Toplevel(self.win)
        win.title("Room List")
        conn = db.get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM rooms")
        rooms = cursor.fetchall()
        cursor.close()
        conn.close()
        for r in rooms:
            tk.Label(win, text=str(r)).pack()

    def update_room(self):
        win = tk.Toplevel(self.win)
        win.title("Update Room")
        tk.Label(win, text="Room Number to Update:").pack()
        room_num_entry = tk.Entry(win)
        room_num_entry.pack()
        tk.Label(win, text="New Status:").pack()
        status_entry = tk.Entry(win)
        status_entry.pack()
        tk.Button(win, text="Update", command=lambda: self.perform_update(room_num_entry.get(), status_entry.get(), win)).pack()

    def perform_update(self, room_number, status, win):
        conn = db.get_connection()
        cursor = conn.cursor()
        cursor.execute("UPDATE rooms SET status=%s WHERE room_number=%s", (status, room_number))
        conn.commit()
        cursor.close()
        conn.close()
        win.destroy()
