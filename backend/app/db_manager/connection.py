import sqlalchemy
from flask import request, jsonify
from app.db_manager import bp

connections = {}

@bp.route('/connect', methods=['POST'])
def connect():
    data = request.get_json()
    db_type = data.get('dbType')
    connection_string = data.get('connectionString')

    try:
        engine = sqlalchemy.create_engine(connection_string)
        connections[db_type] = engine
        return jsonify({"message": "Connection successful"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@bp.route('/list', methods=['GET'])
def list_connections():
    return jsonify(list(connections.keys())), 200