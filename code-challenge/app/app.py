#!/usr/bin/env python3

from flask import Flask, make_response, jsonify, request
from flask_migrate import Migrate


from models import db, Hero

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db/app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

migrate = Migrate(app, db)

db.init_app(app)

heroes = [
    {"id": 1, "name": "Kamala Khan", "super_name": "Ms. Marvel"},
]

@app.route('/heroes', method=['GET'])
def get_heroes():
    return jsonify(heroes)

heroes = {
    1: {
        "name": "Kamala Khan",
        "super_name": "Ms. Marvel",
        "powers": [
            {"id": 1, "name": "super strength", "description": "gives the wielder super-human strengths"},
            {"id": 2, "name": "flight", "description": "gives the wielder the ability to fly through the skies at supersonic speed"}
        ]
    },
}
@app.route('/heroes/<int:hero_id>', methods=['GET'])
def get_heroes(hero_id):
    if heroes:
        return jsonify(heroes)
    else:
        return{404, "Hero not found"}
@app.errorhandler(404)
def hero_not_found(error):
    return jsonify({"error": "Hero not found"}), 404

powers = {
    1: {"name": "super strength", "description": "gives the wielder super-human strengths"},
    2: {"name": "flight", "description": "gives the wielder the ability to fly through the skies at supersonic speed"}
}

# Function to validate power data
def validate_power_data(data):
    errors = []
    if "description" not in data:
        errors.append("Description is required.")
    return errors

@app.route('/powers/<int:power_id>', methods=['PATCH'])
def update_power(power_id):
    power = powers.get(power_id)
    if not power:
        return jsonify({"error": "Power not found"}), 404

    data = request.get_json()
    errors = validate_power_data(data)

    if errors:
        return jsonify({"errors": errors}), 400

    power["description"] = data["description"]
    return jsonify(power)

if __name__ == '__main__':
    app.run(port=5555)
