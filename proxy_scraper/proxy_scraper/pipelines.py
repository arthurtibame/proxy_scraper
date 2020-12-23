# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from scrapy.utils.project import get_project_settings
from scrapy.exceptions import DropItem
import pymongo


class ProxyScraperPipeline:
    def __init__(self) -> None:
        """
        Initial the connection details first 
        """
        settings = get_project_settings()
        connection = pymongo.MongoClient(
            host=settings['MONGODB_SERVER'],
            port=settings['MONGODB_PORT'],
            username=settings['MONGODB_USERNAME'],
            password=settings['MONGODB_PASSWORD']
        )        
        db=connection[settings['MONGODB_DB']]
        self.collection = db[settings['MONGODB_COLLECTION']]

    def process_item(self, item, spider):
        valid = True
        for data in item:
            if not data:
                valid=False
                raise DropItem(f"Missing {data}!")

        if valid:
            try:   

                data = dict(item)
                data['_id'] = data['proxy']                
                self.collection.insert(data)
            except:
                print("proxy exists")
            
        return item
