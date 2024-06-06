from flask import request, jsonify
from app.db_manager import bp, connections

@bp.route('/schema', methods=['GET'])
def get_schema():
    db_type = request.args.get('dbType')
    if db_type not in connections:
        return jsonify({"error": "No connection found"}), 400

    engine = connections[db_type]
    inspector = sqlalchemy.inspect(engine)
    schema = {table_name: [col['name'] for col in inspector.get_columns(table_name)] for table_name in inspector.get_table_names()}

    return jsonify(schema), 200