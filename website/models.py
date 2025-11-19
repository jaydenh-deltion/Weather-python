from flask import Flask 
import sqlite3

with sqlite3.connect('database.db') as conn:
    try:
        with sqlite3.connect('my.db') as conn:
            print(f"Connected to database successfully")
    except sqlite3.Error as e:
        print(f"Database connection failed: {e}")

