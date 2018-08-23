import urllib.request
from bs4 import BeautifulSoup
# from html.parser import HTMLParser
# url = "http://www.8591.com.tw/mobileGame.html"
# url = "http://www.8591.com.tw/mobileGame-list-22042.html?gst=1"
url = "http://www.8591.com.tw/mobileGame-list.html?searchGame=22042&searchServer=&searchType=&searchKey=&firstRow=40"
# http://www.8591.com.tw/mobileGame-list.html?searchGame=22042&searchServer=&searchType=&searchKey=&firstRow=80

fp = urllib.request.urlopen(url)
myby = fp.read()
mystr = myby.decode('utf8')
fp.close()

# print(mystr)
# res = HTMLParser.feed('<p>test</p>')

soup = BeautifulSoup(mystr, 'html.parser')
# print(soup.prettify())


price = soup.select('#wrapper > div > div > div.cl-wrap.c-price')
store = soup.select('#wrapper > div > div > div.cl-wrap.c-store')
pv = soup.select('#wrapper > div > div > div.cl-wrap.c-pv')

items = soup.select('#wrapper > div > div.c-line.clearfix > div.cl-wrap.c-title > div.c-title-line.c-title-head > a')
print(len(items))
for i in items:
    print("\ni="+str(items.index(i)))    
    print('game='+ i.get('date-gamename'))
    print('type='+ i.get('date-waretype'))
    print('title='+ i.get('title'))
    print('url='+ 'http://www.8591.com.tw/'+i.get('href')[2:])
    
    res2 = soup.select('#wrapper > div > div > div.cl-wrap.c-title > div > span.c-title-link')
    detail = res2[items.index(i)].select('a')
    for b in detail:
        print("b"+str(detail.index(b))+"="+b.text)
    
    print("price="+price[items.index(i)].text)
    print("store="+store[items.index(i)].text)
    print("pv="+pv[items.index(i)].text)

# get price, store, pv
# price = soup.select('#wrapper > div > div > div.cl-wrap.c-price')
# store = soup.select('#wrapper > div > div > div.cl-wrap.c-store')
# pv = soup.select('#wrapper > div > div > div.cl-wrap.c-pv')
# for i in price:
#     print(price[price.index(i)].text, store[price.index(i)].text, pv[price.index(i)].text)
    
# res2 = soup.select('#wrapper > div > div > div.cl-wrap.c-title > div > span.c-title-link')
# detail = res2[0].select('a')
# for i in detail:
#     print(str(detail.index(i))+"="+i.text)
