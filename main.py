__author__ = 'akhdir'

from price_getter import *

    # s = scraperFactory.getScraper('souq')

    # s = scraperFactory.getScraper('jadopado')

    # s = scraperFactory.getScraper('apple')

    # s = scraperFactory.getScraper('sharafdg')

    # s = scraperFactory.getScraper('jumbo')

    # s = scraperFactory.getScraper('alshop')

# example
s = getterFactory.getPriceGetter('apple')
price = s.get('http://www.apple.com/ae/shop/buy-iphone/iphone-7/4.7-inch-display-32gb-silver#00,12,20', 'price')

print price

s = getterFactory.getPriceGetter('souq')
price = s.get('http://uae.souq.com/ae-en/apple-iphone-7-with-facetime-32gb-4g-lte-silver-11526713/i/', 'price')

print price

s = getterFactory.getPriceGetter('jumbo')
price = s.get('http://www.jumbo.ae/gaming-pcs/hp-omen-17-w000ne-i7-16gb-2tb-17/p-0441617-29758057822-cat.html#variant_id=0441617-29758057822', 'price')

print price



