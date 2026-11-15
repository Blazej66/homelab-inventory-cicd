import os
from flask import Flask, jsonify, request
from sqlalchemy import text
from sqlalchemy.orm import sessionmaker

from app.models import  db, Device

def create_app(database_url=None):
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = database_url or os.getenv(
        "DATABASE_URL", "sqlite:///local_dev.db")

    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    with app.app_context():
        db.create_all()

    @app.route("/health", methods=["GET"])
    def health_check():
        try:
            db.session.execute(text("SELECT 1"))
            return jsonify({"status": "healthy", "database": "connected"}), 200
        except Exception:
            return jsonify({"status": "unhealthy", "database": "disconnected"}), 503


    @app.route("/api/devices", methods=["GET"])
    def get_devices():
        devices = Device.query.all()
        return jsonify([d.to_dict() for d in devices]), 200

    @app.route("/api/devices", methods=["POST"])
    def add_device():
        data = request.get_json() or {}
        if not data.get("hostname") or not data.get("ip_address") or not data.get("role"):
            return jsonify({"error": "hostname, ip_address and role are required"}), 400


        device = Device(
            hostname=data["hostname"],
            ip_address=data["ip_address"],
            vlan=data.get("vlan"),
            role=data["role"],
        )
        db.session.add(device)
        db.session.commit()
        return jsonify({"device": device.to_dict()}), 201

    @app.route("/api/devices/<int:device_id>", methods=["DELETE"])
    def delete_device(device_id):
        device = db.session.get(Device, device_id)
        if not device:
            return jsonify({"error": "device not found"}), 404
        db.session.delete(device)
        db.session.commit()
        return jsonify({"message": "device deleted"}), 200

    return app

app = create_app()