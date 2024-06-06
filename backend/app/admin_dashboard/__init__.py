from flask import Blueprint

bp = Blueprint('admin_dashboard', __name__)

from app.admin_dashboard import management