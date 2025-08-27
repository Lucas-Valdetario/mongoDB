from datetime import datetime  # ← Corrigido: datetime em vez de date
from src.models.repository.interfaces.orders_repository import OrdersRepositoryInterface
from src.main.http_types.http_request import HttpRequest
from src.main.http_types.http_response import HttpResponse

class RegistryOrder:
    def __init__(self, orders_repository: OrdersRepositoryInterface) -> None:
        self.__orders_repository = orders_repository

    def registry(self, http_request: HttpRequest) -> HttpResponse:
        try:    
            body = http_request.body
            new_order = self.__format_new_order(body)
            self.__registry_order(new_order)

            return self.__format_response(new_order)  # ← Mantido como estava
        except Exception as exception:
            return HttpResponse(
                body= {"error": str(exception)},  # ← Melhor converter para string
                status_code=400
            )
            
    def __format_new_order(self, body: dict) -> dict:
        new_order = body["data"]
        new_order = { **new_order, "created_at": datetime.now() }
        return new_order

    def __registry_order(self, new_order: dict) -> None:
        self.__orders_repository.insert_document(new_order)

    def __format_response(self, new_order: dict) -> HttpResponse:  # ← Corrigido: adicionado parâmetro
        return HttpResponse(
            body={
                "data": {
                    "type": "Order",
                    "count": 1,  # ← Corrigido: minúsculo para coincidir com o teste
                    "registry": True
                }
            },
            status_code=201
        )