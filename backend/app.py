from flask import Flask, request, jsonify
from flask_cors import CORS
import sqlite3

app = Flask(__name__)
CORS(app)

def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

# Endpoint: lista klientów
@app.route('/clients', methods=['GET'])
def get_clients():
    conn = get_db_connection()
    clients = conn.execute('SELECT * FROM clients').fetchall()
    conn.close()
    return jsonify([dict(row) for row in clients])

# Endpoint: dodanie klienta
@app.route('/clients', methods=['POST'])
def add_client():
    data = request.json
    conn = get_db_connection()
    conn.execute('INSERT INTO clients (name, email, phone, status) VALUES (?, ?, ?, ?)',
                 (data['name'], data['email'], data['phone'], data['status']))
    conn.commit()
    conn.close()
    return jsonify({'message': 'Client added successfully'}), 201

# Endpoint: interakcje (notatki)
@app.route('/interactions/<int:client_id>', methods=['GET'])
def get_interactions(client_id):
    conn = get_db_connection()
    interactions = conn.execute('SELECT * FROM interactions WHERE client_id = ?', (client_id,)).fetchall()
    conn.close()
    return jsonify([dict(row) for row in interactions])

@app.route('/interactions', methods=['POST'])
def add_interaction():
    data = request.json
    conn = get_db_connection()
    conn.execute('INSERT INTO interactions (client_id, note, interaction_date) VALUES (?, ?, ?)',
                 (data['client_id'], data['note'], data['interaction_date']))
    conn.commit()
    conn.close()
    return jsonify({'message': 'Interaction added'}), 201

# Endpoint: edycja notatki
@app.route('/interactions/<int:interaction_id>', methods=['PUT'])
def update_interaction(interaction_id):
    data = request.json
    conn = get_db_connection()
    conn.execute('UPDATE interactions SET note = ?, interaction_date = ? WHERE id = ?',
                 (data['note'], data['interaction_date'], interaction_id))
    conn.commit()
    conn.close()
    return jsonify({'message': 'Interaction updated successfully'}), 200

# Endpoint: usunięcie notatki
@app.route('/interactions/<int:interaction_id>', methods=['DELETE'])
def delete_interaction(interaction_id):
    conn = get_db_connection()
    conn.execute('DELETE FROM interactions WHERE id = ?', (interaction_id,))
    conn.commit()
    conn.close()
    return jsonify({'message': 'Interaction deleted successfully'}), 200

# Endpoint: edycja klienta
@app.route('/clients/<int:client_id>', methods=['PUT'])
def update_client(client_id):
    data = request.json
    conn = get_db_connection()
    conn.execute('''
        UPDATE clients 
        SET name = ?, email = ?, phone = ?, status = ? 
        WHERE id = ?
    ''', (data['name'], data['email'], data['phone'], data['status'], client_id))
    conn.commit()
    conn.close()
    return jsonify({'message': 'Client updated successfully'}), 200


if __name__ == '__main__':
    app.run(debug=True)