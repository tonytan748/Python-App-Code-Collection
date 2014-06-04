from soup import BeautifulSoup as bs
from scrapy.http import Request
from scrapy.spider import BaseSpider
from scrapy01.items import Scrapy01Item

class Scrapy01Spider(BaseSpider):
    name='scrapy01'
    allowed_domains=[]
    start_urls=['http://news.ycombinator.com']
    
    def parse(self,response):
        if 'news.ycombinator.com' in response.url:
            soup=bs(response.body)
            items=[(x[0].text,x[0].get('href')) for x in 
                   filter(None,[x.findChildren() for x in 
                       soup.findAll('td',{'class':'title'})])]

            for item in items:
                print item
                scrapy01_item=Scrapy01Item()
                scrapy01_item['title']=item[0]
                scrapy01_item['link']=item[1]
                try:
                    yield Request(item[1],callback=self.parse)
                except ValueError:
                    yield Request('http://news.ycombinator.com/' + item[1],callback=self.parse)
                yield scrapy01_item
'''
        sel=Selector(response)
        sites=sel.xpath('//td[@class='title']')
        for site in sites:
            title=site.xpath('a/text()').extract()
            link=site.xpath('a/@href').extract()
            print title,link
'''
