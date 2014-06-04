# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from sqlalchemy.orm import sessionmaker
from models import Scrapy01,db_connect,create_scrapy01_table

class Scrapy01Pipeline(object):
    def __init__(self):
        engine=db.connect()
        create_scrapy01_table(engine)
        self.Session=sessionmaker(bind=engine)

    def process_item(self, item, spider):
        session=self.Session()
        scrapy01=Scrapy01(**item)
        session.add(scrapy01)
        session.commit()
        return item
