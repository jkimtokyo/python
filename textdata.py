# config=utf-8
import urllib.request
page = urllib.request.urlopen('http://beans-r-us.appspot.com/prices.html')
text = page.read().decode('utf8')
price = text[233:238]
print('소비가:', price)

import urllib.request
page = urllib.request.urlopen('http://beans-r-us.appspot.com/prices-loyalty.html')
text = page.read().decode('utf8')
finds = text.find('$')
startprice = finds+0
endprice = finds+5
price = text[startprice:endprice]
print('도매가:', price)
print('')

msg = 'Monster truck rally. 4pm. monday'
print(msg.upper())
print('-Lower case:', msg.lower())
pmwhere = '-Where 4PM be in the sentence?'
print(pmwhere, msg.find('4pm'))
whattime = '-Can I ask what that time is?'
print(whattime, msg[21:25])

print('---------')
import urllib.request
price = 9.99
while price > 4.74:
    page = urllib.request.urlopen('http://beans-r-us.appspot.com/prices-loyalty.html')
    text = page.read().decode('utf8')
    finds = text.find('$')
    startprice = finds+1
    endprice = finds+5
    price = float(text[startprice:endprice]) # 텍스트 이건 스트링이니까 타입에러 (변수형이 안 맞음) 발생한다
print(price, ',Buy Now!')

