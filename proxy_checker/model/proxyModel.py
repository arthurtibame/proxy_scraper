import pymongo
from pymongo import collection
from utils import settings

class ProxyModel:
    def __init__(self, collection:str) -> None:
        connection=pymongo.MongoClient(
            host=settings.MONGODB_SERVER,
            port=settings.MONGODB_PORT,
            username=settings.MONGODB_USERNAME,
            password=settings.MONGODB_PASSWORD,
        )
        self.__collection=collection
        self.db=connection[settings.MONGODB_DB]
        self.collection=self.db[collection]

    def get_all_data(self):
        return self.collection.find({})

    def insert(self, item:dict) -> None:
        self.collection.insert(item)
    
    def drop_collection(self) -> None:
        self.db.drop_collection(self.__collection)
    


