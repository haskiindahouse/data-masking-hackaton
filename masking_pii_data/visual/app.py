from flask import Flask, render_template, jsonify, request
import psycopg2
import os

app = Flask(__name__)

def get_db_connection(dbname=None):
    conn = psycopg2.connect(
        dbname=dbname or os.getenv('POSTGRES_DB'),
        user=os.getenv('POSTGRES_USER'),
        password=os.getenv('POSTGRES_PASSWORD'),
        host=os.getenv('DB_HOST', 'localhost'),
        port=os.getenv('DB_PORT', '5432')
    )
    return conn

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/databases')
def databases():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT datname FROM pg_database WHERE datistemplate = false;")
    databases = [row[0] for row in cursor.fetchall()]
    cursor.close()
    conn.close()
    return jsonify(databases)

@app.route('/tables')
def tables():
    db_name = request.args.get('db_name')
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(f"SELECT table_name FROM information_schema.tables WHERE table_schema='public';")
    tables = [row[0] for row in cursor.fetchall()]
    cursor.close()
    conn.close()
    return jsonify(tables)

@app.route('/table_structure')
def table_structure():
    db_name = request.args.get('db_name')
    table_name = request.args.get('table_name')
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute(f"SELECT column_name, data_type FROM information_schema.columns WHERE table_name = '{table_name}';")
    columns = cursor.fetchall()

    cursor.execute(f"""
        SELECT
            kcu.column_name,
            ccu.table_name AS foreign_table_name,
            ccu.column_name AS foreign_column_name
        FROM
            information_schema.table_constraints AS tc
            JOIN information_schema.key_column_usage AS kcu
              ON tc.constraint_name = kcu.constraint_name
              AND tc.table_schema = kcu.table_schema
            JOIN information_schema.constraint_column_usage AS ccu
              ON ccu.constraint_name = tc.constraint_name
        WHERE constraint_type = 'FOREIGN KEY' AND tc.table_name='{table_name}';
    """)
    foreign_keys = cursor.fetchall()

    cursor.close()
    conn.close()

    return jsonify({
        'table_name': table_name,
        'columns': columns,
        'foreign_keys': foreign_keys
    })

if __name__ == '__main__':
    app.run(debug=True)
