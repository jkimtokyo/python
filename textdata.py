# config=utf-8

import urllib.request
page = urllib.request.urlopen('http://beans-r-us.appspot.com/prices.html')
text = page.read().decode('utf8')
price = text[233:238]
print(price)

import urllib.request
page = urllib.request.urlopen('http://beans-r-us.appspot.com/prices-loyalty.html')
text = page.read().decode('utf8')
price = text[233:238]
print(price)
print('')

msg = 'Monster truck rally. 4pm. monday'
print(msg.upper())
print('-Lower case:', msg.lower())
pmwhere = '-Where 4PM be in the sentence?'
print(pmwhere, msg.find('4pm'))
whattime = '-Can I ask what that time is?'
print(whattime, msg[21:25])

