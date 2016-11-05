from webscraping import download, xpath
from math import ceil
from html_parser import *


class getterFactory:

    @staticmethod
    def getPriceGetter(scraperType):
        classname = scraperType+'PriceGetter'
        constructor = globals()[classname]
        instance = constructor()
        return instance

class PriceGetter:

    def get(self, url, info):
        print url
        print info

    def cleanUp(self, data):
        data = data.replace( 'AED','')
        data = data.strip()
        data = data.replace(",","")
        return data


    def toInt(self, price):
        try:
            price = int(float(price))
        except ValueError:
            price = 0
        return price


class souqPriceGetter(PriceGetter):

    def get(self, url, info):
        D = download.Download(read_cache=False, write_cache=False)
        html = D.get(url)
        if info == 'price':
            # data = xpath.get(html, '//div[@class="price-holder xlarg-price"]//', remove=('span','/span'))
            data = xpath.get(html, '//h3[@class="price"]//')
            parser = SouqHTMLParser()
            parser.feed(data)
            price = self.cleanUp(parser.price)
        return  self.toInt(price)

class jadopadoPriceGetter(PriceGetter):

    def get(self, url, info):
        D = download.Download(read_cache=False, write_cache=False)
        html = D.get(url)
        if info == 'price':
            data = xpath.get(html, '//span[@class="new_price"]//')
            data = self.cleanUp(data)
            if data == '':
                data = xpath.get(html, '//span[@class="regular_price"]//')
                data = self.cleanUp(data)
        return self.toInt(data)

class applePriceGetter(PriceGetter):

    def get(self, url, info):
        D = download.Download(read_cache=False, write_cache=False)
        html = D.get(url)
        if info == 'price':
            data = xpath.get(html, '//div[@class="item equalize-capacity-button-height selection"]//')
            parser = AppleHTMLParser()
            parser.feed(data)
            data = self.cleanUp(parser.price)
        return  self.toInt(data)

class sharafdgPriceGetter(PriceGetter):

    def get(self, url, info):
        D = download.Download(read_cache=False, write_cache=False)
        html = D.get(url)
        if info == 'price':
            data = xpath.get(html, '//span[@class="sh-price-total"]//')
            data = self.cleanUp(data)
        return self.toInt(data)


class jumboPriceGetter(PriceGetter):

    def get(self, url, info):
        D = download.Download(read_cache=False, write_cache=False)
        html = D.get(url)
        if info == 'price':
            data = xpath.get(html, '//div[@class="our_price"]//')
            parser = JumboHTMLParser()
            parser.feed(data)
            data = parser.price
            data = self.cleanUp(data)
        return self.toInt(data)

class alshopPriceGetter(PriceGetter):

    def get(self, url, info):
        D = download.Download(read_cache=False, write_cache=False)
        html = D.get(url)
        if info == 'price':
            data = xpath.get(html, '//p[@class="special-price"]//')
            parser = AlShopHTMLParser()
            parser.feed(data)
            data = parser.price
            data = self.cleanUp(data)
        return self.toInt(data)

