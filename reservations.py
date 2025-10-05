import tkinter as tk
import db

class ReservationsWindow:
    def __init__(self):
        self.win = tk.Toplevel()
        self.win.title("Manage Reservations")
        tk.Button(self.win, text="Add Reservation", command=self.add_reservation).pack()
        tk.Button(self.win, text="View Reservations", command=self.view_reservations).pack()
        tk.Button(self.win, text="Update Reservation", command=self.update_reservation).pack()

    def add_reservation(self):
        win = tk.Toplevel(self.win)
        win.title("Add Reservation")
        tk.Label(win, text="Room ID:").pack()
        room_id_entry = tk.Entry(win)
        room_id_entry.pack()
        tk.Label(win, text="Guest Name:").pack()
        name_entry = tk.Entry(win)
        name_entry.pack()
        tk.Label(win, text="Start Date (YYYY-MM-DD):").pack()
        start_entry = tk.Entry(win)
        start_entry.pack()
        tk.Label(win, text="End Date (YYYY-MM-DD):").pack()
        end_entry = tk.Entry(win)
        end_entry.pack()
        tk.Label(win, text="Total:").pack()
        total_entry = tk.Entry(win)
        total_entry.pack()
        tk.Button(win, text="Submit", command=lambda: self.save_reservation(room_id_entry.get(), name_entry.get(), start_entry.get(), end_entry.get(), total_entry.get(), win)).pack()

    def save_reservation(self, room_id, guest_name, start_date, end_date, total, win):
        conn = db.get_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO reservations (room_id, guest_name, start_date, end_date, total) VALUES (%s, %s, %s, %s, %s)", (room_id, guest_name, start_date, end_date, total))
        conn.commit()
        cursor.close()
        conn.close()
        win.destroy()

    def view_reservations(self):
        win = tk.Toplevel(self.win)
        win.title("Reservations List")
        conn = db.get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM reservations")
        reservations = cursor.fetchall()
        cursor.close()
        conn.close()
        for r in reservations:
            tk.Label(win, text=str(r)).pack()

    def update_reservation(self):
        win = tk.Toplevel(self.win)
        win.title("Update Reservation")
        tk.Label(win, text="Reservation ID to Update:").pack()
        res_id_entry = tk.Entry(win)
        res_id_entry.pack()
        tk.Label(win, text="New End Date (YYYY-MM-DD):").pack()
        end_entry = tk.Entry(win)
        end_entry.pack()
        tk.Button(win, text="Update", command=lambda: self.perform_update(res_id_entry.get(), end_entry.get(), win)).pack()

    def perform_update(self, res_id, end_date, win):
        conn = db.get_connection()
        cursor = conn.cursor()
        cursor.execute("UPDATE reservations SET end_date=%s WHERE id=%s", (end_date, res_id))
        conn.commit()
        cursor.close()
        conn.close()
        win.destroy()
