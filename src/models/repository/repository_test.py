from src.models.connection.connection_handler import DBConnectionHandler
from .orders_repository import OrdersRepository

db_connection_handler = DBConnectionHandler()
db_connection_handler.connect_to_db()
conn = db_connection_handler.get_db_connection()

def test_insert_document():
    orders_repository = OrdersRepository(conn)
    my_doc = {"order_id": 1, "customer_name": "John Doe", "items": ["item1", "item2"], "total": 100.0}
    orders_repository.insert_document(my_doc)

def test_insert_list_of_documents():
    orders_repository = OrdersRepository(conn)
    my_doc = [{"elem1":"aqui"}, {"elem2": "aqui2"}, {"elem3": "aqui3"}]
    orders_repository.insert_list_of_documents(my_doc)