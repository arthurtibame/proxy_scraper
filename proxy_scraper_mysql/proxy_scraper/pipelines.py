# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from scrapy.utils.project import get_project_settings
from scrapy.exceptions import DropItem
import pymysql


class ProxyScraperPipeline:
    def __init__(self) -> None:
        """
        Initial the connection details first 
        """
        settings = get_project_settings()
        self.db = pymysql.connect(
            host=settings['MYSQL_SERVER'],
            port=settings['MYSQL_PORT'],
            user=settings['MYSQL_USERNAME'],
            password=settings['MYSQL_PASSWORD'],
            db=settings['MYSQL_DB']
        )                
        self.cursor = self.db.cursor()
    def process_item(self, item, spider):
        valid = True
        for data in item:
            if not data:
                valid=False
                raise DropItem(f"Missing {data}!")

        if valid:
            try:   
                data = dict(item)                
                sql='''
                    INSERT INTO proxy_pool (proxy, scheme, port)
                    VALUES (%s, %s, %s)
                '''
                self.cursor.execute(sql, (data['proxy'], data['scheme'], data['port']))
                self.db.commit()
            except Exception as e :
                print(e)
            
        return item

    def close_spider(self, spider):
        self.cursor.close()
        self.db.close()