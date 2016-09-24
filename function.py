#config=utf-8

import urllib.request
def getprice():
    page = urllib.request.urlopen('http://beans-r-us.appspot.com/prices-loyalty.html')
    text = page.read().decode('utf-8')
    where = text.find('$')
    startprice = where+1
    endprice = where+5
    return(text[startprice:endprice])

price = getprice()
discount = 0.9
realprice = float(price) * discount
print(realprice)

