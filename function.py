#config=utf-8
import urllib.request
import time

def getprice():
    page = urllib.request.urlopen('http://beans-r-us.appspot.com/prices-loyalty.html')
    text = page.read().decode('utf-8')
    where = text.find('$')
    startprice = where+1
    endprice = where+5
    return float (text[startprice:endprice]) #return 이 함수를 다른 곳에서 쓸테니까 리턴해서 함수 호출한 곳으로 데이터를 보낸다.여기서 값은 소수점이니까 'float''''

yesorno = input("Want to know Coffee price now?: ")
if yesorno == 'y':
    print('Now price is:', getprice())
elif yesorno == 'n':
    price = 99.99
    while price > 4.4:
        time.sleep(3)
        price = getprice()
    print('Discount Price is:', price)
else:
    print('Please enter the code Y or N')