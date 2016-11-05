# web-price-extraction
web-price-extraction extracts the prices from several e-commerce sites in the middle east.
Available sites are:
1- Souq.com 
2- JadoPado
3- Apple UAE Store
4- Sharafd
5- Jumbo Electronics
6- AlShop 


Here is how to use the price_getter: 

```Python from price_getter import *```

# example Apple
```Python
s = getterFactory.getPriceGetter('apple')
price = s.get('http://www.apple.com/ae/shop/buy-iphone/iphone-7/4.7-inch-display-32gb-silver#00,12,20', 'price')
```
# example Souq

```Python
s = getterFactory.getPriceGetter('souq')
price = s.get('http://uae.souq.com/ae-en/apple-iphone-7-with-facetime-32gb-4g-lte-silver-11526713/i/', 'price')
```

# example Jumbo

```Python
s = getterFactory.getPriceGetter('jumbo')
price = s.get('http://www.jumbo.ae/gaming-pcs/hp-omen-17-w000ne-i7-16gb-2tb-17/p-0441617-29758057822-cat.html#variant_id=0441617-29758057822', 'price')
```
