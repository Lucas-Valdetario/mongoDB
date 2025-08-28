from .registry_order_validator import registry_order_validator
import pytest

def test_registry_order_validator():
    body = {
        "data": {
            "name": "example_test",
            "address": "rua test",
            "cupom": False,
            "items": [
                {"item": "Refrigerante", "quantidade": 2},
                {"item": "Batata Frita", "quantidade": 1}
            ]
        }
    }
    registry_order_validator(body)

def test_registry_order_validator_with_errors():
    body_with_error = {
        "data": {
            "name": "example_test",
            "address": "rua test",
            "cupom": "error",
            "items": [
                {"item": "Refrigerante", "quantidade": 2},
                {"item": "Batata Frita", "quantidade": 1}
            ]
        }
    }
    with pytest.raises(Exception):
        registry_order_validator(body_with_error)