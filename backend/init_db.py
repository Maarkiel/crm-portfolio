import sqlite3

conn = sqlite3.connect('database.db')
cursor = conn.cursor()

# Tabela klientów
cursor.execute('''
    CREATE TABLE clients (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        email TEXT,
        phone TEXT,
        status TEXT
    )
''')

# Tabela interakcji
cursor.execute('''
    CREATE TABLE interactions (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        client_id INTEGER,
        note TEXT,
        interaction_date TEXT,
        FOREIGN KEY (client_id) REFERENCES clients (id)
    )
''')

conn.commit()
conn.close()
print("Baza danych gotowa!")
