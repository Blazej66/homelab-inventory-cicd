from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Device(db.Model):

    __tablename__= "devices"

    id = db.Column(db.Integer, primary_key=True)
    hostname = db.Column(db.String(100), unique=True, nullable=False)
    ip_address = db.Column(db.String(45), unique=True, nullable=False)
    role = db.Column(db.String(50), nullable=False)
    vlan = db.Column(db.Integer, nullable=True)

    def to_dict(self):
        return {
            "id": self.id,
            "hostname": self.hostname,
            "ip_address": self.ip_address,
            "role": self.role,
            "vlan": self.vlan,
        }
