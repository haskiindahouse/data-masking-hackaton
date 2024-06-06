from flask import request, jsonify
from app.anonymization import bp


@bp.route('/anonymize', methods=['POST'])
def anonymize():
    data = request.get_json()
    tables = data.get('tables')
    columns = data.get('columns')

    # Implement your anonymization logic here
    anonymized_data = {
        "tables": tables,
        "columns": columns
    }

    return jsonify(anonymized_data), 200