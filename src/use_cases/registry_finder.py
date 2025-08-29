from src.main.http_types import http_request
from src.main.http_types import http_response
from src.models.repository.interfaces.orders_repository import OrdersRepository
from src.main.http_types.http_request import HttpRequest
from src.main.http_types.http_response import HttpResponse
from src.errors.types.http_not_found import HttpNotFound
from src.errors.error_handler import error_handler

class RegistryFinder:
    def __init__(self, orders_repository: OrdersRepository) -> None:
        self.__orders_repository = orders_repository

    def find(self, http_request: HttpRequest) -> HttpResponse:
        try:
            order_id = http_request.path_params["order_id"]
            return self.__search_order(order_id)
        except Exception as exception:
            return error_handler(exception)

    def __search_order(self, order_id: str) -> dict:
        order = self.__orders_repository.select_by_object_id(order_id)
        if not order: raise HttpNotFound("Order not found")
        return order

    def __format_response(self, order: dict) -> HttpResponse:
        return HttpResponse(
            body={
                "data": {
                    "count": 1,
                    "type": "Order",
                    "attributes": order
                }
            },
            status_code=200
        )