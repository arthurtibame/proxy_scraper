from scrapy import item
from bs4 import BeautifulSoup
import scrapy
from proxy_scraper.items import ProxyScraperItem

class scrapyProxy(scrapy.Spider):
    name ='proxy'
    allowed_domains = ['www.us-proxy.org']
    url = 'https://httpbin.org/ip'
    start_urls = ['https://www.us-proxy.org/']

    def parse(self, response):
        item = ProxyScraperItem()
        soup = BeautifulSoup(response.text, 'lxml')
        trs = soup.select("#proxylisttable tr")
        for tr in trs:
            tr_soup = BeautifulSoup(str(tr), 'lxml')
            tds = tr_soup.select("td")
            if len(tds) > 6:
                ip = tds[0].text
                port = tds[1].text
                anonymity = tds[4].text
                ifScheme = tds[6].text
                if ifScheme == 'yes': 
                    scheme = 'https'
                else: scheme = 'http'
                proxy = "%s://%s:%s"%(scheme, ip, port)
                # if anonymity != 'anonymous' and scheme == 'https':
                # if scheme == 'https':                         
                item['scheme']=scheme
                item['proxy']=proxy
                item['port']=port
                yield item