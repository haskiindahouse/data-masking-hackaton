from app import db

class AnonymizationRecord(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    table_name = db.Column(db.String(64))
    column_name = db.Column(db.String(64))
    original_value = db.Column(db.String(256))
    anonymized_value = db.Column(db.String(256))