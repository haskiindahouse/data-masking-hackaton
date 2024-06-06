from flask import Blueprint

bp = Blueprint('anonymization', __name__)

from app.anonymization import engine