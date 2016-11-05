from HTMLParser import HTMLParser

class SouqHTMLParser(HTMLParser):
    
    def __init__(self):
        HTMLParser.__init__(self)
        self.price = ''
        self.count = 0

    def handle_data(self, data):

        self.count += 1
        if self.count == 2:
            self.price = data

class AppleHTMLParser(HTMLParser):
    
    def __init__(self):
        HTMLParser.__init__(self)
        self.pricetag = 0
        self.count = 0
        self.price = ''

    def handle_starttag(self, tag, attrs):
        if tag == 'span':
            for name, value in attrs:
                if name == 'class' and value == 'current_price':
                    self.count +=1
                    self.pricetag = 1
                else:
                    self.pricetag = 0

    def handle_data(self, data):
        tmp = data.strip()
        if self.pricetag == 1 and self.count == 1 and tmp != '':
            self.price = tmp


class AlShopHTMLParser(HTMLParser):
    
    def __init__(self):
        HTMLParser.__init__(self)
        self.pricetag = 0
        self.count = 0
        self.price = ''

    def handle_starttag(self, tag, attrs):
        if tag == 'span':
            for name, value in attrs:
                if name == 'class' and value == 'price':
                    self.count +=1
                    self.pricetag = 1

    def handle_data(self, data):
        tmp = data.strip()
        if self.pricetag == 1 and tmp != '' :
            print tmp
            self.price = tmp


class JumboHTMLParser(HTMLParser):
    
    def __init__(self):
        HTMLParser.__init__(self)
        self.count = 0
        self.price = ''

    def handle_starttag(self, tag, attrs):
        if tag == 'span':
            self.count += 1

    def handle_data(self, data):
        if self.count == 3:
            self.price = data
