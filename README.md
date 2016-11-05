# price-extraction
price-extraction extracts the prices from several e-commerce sites in the middle east.
Available sites are:
* Apple UAE Store
* Souq.com 
* JadoPado
* Sharafd
* Jumbo Electronics
* AlShop 

More to come...

# Price Getter Class
price getter class will get you the price of any product listed on one of the above site, by just providing the link to that product.


```Python 
from price_getter import *
```

# example Apple
```Python
s = getterFactory.getPriceGetter('apple')
price = s.get('http://www.apple.com/ae/shop/buy-iphone/iphone-7/4.7-inch-display-32gb-silver#00,12,20')
```
# example Souq

```Python
s = getterFactory.getPriceGetter('souq')
price = s.get('http://uae.souq.com/ae-en/apple-iphone-7-with-facetime-32gb-4g-lte-silver-11526713/i/')
```

# example Jumbo

```Python
s = getterFactory.getPriceGetter('jumbo')
price = s.get('http://www.jumbo.ae/gaming-pcs/hp-omen-17-w000ne-i7-16gb-2tb-17/p-0441617-29758057822-cat.html#variant_id=0441617-29758057822')
```
