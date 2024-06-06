from flask import Blueprint

bp = Blueprint('db_manager', __name__)

from app.db_manager import connection, schema