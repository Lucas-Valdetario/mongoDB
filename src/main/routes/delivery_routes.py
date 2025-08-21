from flask import Blueprint, jsonify, request

delivery_routes = Blueprint('delivery_routes', __name__)

@delivery_routes.route('/deliveries', methods=['POST'])
def registry_order():
    print(request.json)
    return jsonify({"ola": "mundo"}), 200
