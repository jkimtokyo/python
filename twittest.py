import tweepy
import time
import urllib

def send_to_twitter():
	msg = "I am a message that will be sent to Twitter"
	password_manager = urllib.request.HTTPPasswordMgr()
	password_manager.add_password("Twitter API",
	"http://twitter.com/statuses", "...", "...")
	http_handler = urllib.request.HTTPBasicAuthHandler(password_manager)
	page_opener = urllib.request.build_opener(http_handler)
	urllib.request.install_opener(page_opener)
	params = urllib.parse.urlencode( {'status': msg} )
	resp = urllib.request.urlopen("http://twitter.com/statuses/update.json", params)
	resp.read()

def get_price():
    page = urllib.request.urlopen("http://beans-r-us.appspot.com/prices-loyalty.html")
    text = page.read().decode("utf-8")
    where = text.find('$')
    start_of_price = where + 1
    end_of_price = start_of_price + 4
    return float(text[start_of_price:end_of_price])

price_now = input("Do you want to see the price now (Y/N)? ")

if price_now == "Y":
    send_to_twitter(get_price())
    #print('Now price is:', get_price())
else:
    price = 99.99
    while price > 4.74:
        time.sleep(9)
        price = get_price()
    send_to_twitter("Buy!")
