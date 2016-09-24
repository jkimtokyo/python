# config = utf-8

import time
import urllib.request
price = 9.99
while price > 4.74:
    time.sleep(10)
    page = urllib.request.urlopen('http://beans-r-us.appspot.com/prices-loyalty.html')
    text = page.read().decode('utf8')
    finds = text.find('$')
    startprice = finds+1
    endprice = finds+5
    price = float(text[startprice:endprice]) # 텍스트 이건 스트링이니까 타입에러 (변수형이 안 맞음) 발생한다

print(price,': Buy Now!')

