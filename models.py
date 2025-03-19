from database import db

class AllowedMachine(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    hostname = db.Column(db.String(255), nullable=False)
    mac = db.Column(db.String(255), unique=True, nullable=False)
    expiry_date = db.Column(db.DateTime, nullable=False)


class PendingMachine(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    hostname = db.Column(db.String(255), nullable=False)
    mac = db.Column(db.String(255), unique=True, nullable=False)
