from flask import Flask, request, jsonify
import sqlite3

app = Flask(_name_)

# Connect to the database
conn = sqlite3.connect('certificates.db')
cursor = conn.cursor()

# Create a table if it doesn't exist
cursor.execute('''
    CREATE TABLE IF NOT EXISTS certificates (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        certificate_id TEXT,
        name TEXT,
        date_of_issue TEXT,
        other_details TEXT
    )
''')
conn.commit()

@app.route('/verify', methods=['POST'])
def verify_certificate():
    certificate_id = request.json['certificate_id']
    cursor.execute('SELECT * FROM certificates WHERE certificate_id = ?', (certificate_id,))
    result = cursor.fetchone()

    if result:
        return jsonify({'name': result[1], 'date_of_issue': result[2], 'other_details': result[3]})
    else:
        return jsonify({'error': 'Certificate not found'})

if _name_ == '_main_':
    app.run(debug=True)
