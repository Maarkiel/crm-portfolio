import sqlite3
import os

# Jeśli plik istnieje – usuń go (czyści bazę)
if os.path.exists("database.db"):
    os.remove("database.db")

conn = sqlite3.connect('database.db')
cursor = conn.cursor()

# 🧑‍💼 Tabela klientów
cursor.execute('''
    CREATE TABLE clients (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        email TEXT,
        phone TEXT,
        status TEXT
    )
''')

# 📝 Tabela interakcji (notatek)
cursor.execute('''
    CREATE TABLE interactions (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        client_id INTEGER NOT NULL,
        note TEXT,
        interaction_date TEXT,
        FOREIGN KEY (client_id) REFERENCES clients (id) ON DELETE CASCADE
    )
''')

conn.commit()
conn.close()
print("✅ Baza danych została utworzona i wyczyszczona.")
