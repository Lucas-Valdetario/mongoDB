from flask import Blueprint, jsonify, request
from src.main.http_types.http_request import HttpRequest

delivery_routes = Blueprint('delivery_routes', __name__)

@delivery_routes.route('/deliveries', methods=['POST'])
def registry_order():
    print(request.json)
    http_request = HttpRequest(body=request.json)
    return jsonify({"ola": "mundo"}), 200
