from pymongo import MongoClient

class DBConnectionHandler:
    def __init__(self) -> None:
        self.__connection_string = 'mongodb://{}:{}@{}:{}/?authSource=admin'.format()