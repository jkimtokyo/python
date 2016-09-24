#config=utf-8

import urllib.request
def getprice():
    page = urllib.request.urlopen('http://beans-r-us.appspot.com/prices-loyalty.html')
    text = page.read().decode('utf-8')
    where = text.find('$')
    startprice = where+0
    endprice = where+5
    print(text[startprice:endprice])
getprice()



