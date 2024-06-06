from flask import request, jsonify
from app import db
from app.admin_dashboard import bp
from app.auth.models import User

@bp.route('/create-user', methods=['POST'])
def create_user():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    if User.query.filter_by(username=username).first():
        return jsonify({"error": "User already exists"}), 400
    user = User(username=username)
    user.set_password(password)
    db.session.add(user)
    db.session.commit()
    return jsonify({"message": "User created successfully"}), 201

@bp.route('/delete-user', methods=['DELETE'])
def delete_user():
    data = request.get_json()
    username = data.get('username')
    user = User.query.filter_by(username=username).first()
    if not user:
        return jsonify({"error": "User not found"}), 400
    db.session.delete(user)
    db.session.commit()
    return jsonify({"message": "User deleted successfully"}), 200

@bp.route('/settings', methods=['GET', 'POST'])
def manage_settings():
    # Implement your settings management logic here
    if request.method == 'GET':
        settings = {}  # Fetch current settings
        return jsonify(settings), 200
    elif request.method == 'POST':
        new_settings = request.get_json()
        # Update settings
        return jsonify({"message": "Settings updated"}), 200
```