# db.py
import mysql.connector

def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="your_password",
        database="hotel_db"
    )

def create_tables():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INT AUTO_INCREMENT PRIMARY KEY,
            username VARCHAR(30) UNIQUE,
            password VARCHAR(30),
            name VARCHAR(50)
        )
    """)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS rooms (
            id INT AUTO_INCREMENT PRIMARY KEY,
            room_number INT UNIQUE,
            room_type VARCHAR(20),
            price DECIMAL(10,2),
            status VARCHAR(10)
        )
    """)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS reservations (
            id INT AUTO_INCREMENT PRIMARY KEY,
            room_id INT,
            guest_name VARCHAR(50),
            start_date DATE,
            end_date DATE,
            total DECIMAL(10,2),
            FOREIGN KEY (room_id) REFERENCES rooms(id)
        )
    """)
    conn.commit()
    cursor.close()
    conn.close()
