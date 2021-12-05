import requests
from bs4 import BeautifulSoup
url = "http://www.cntour.cn/"
page=requests.get(url)
soup = BeautifulSoup(page.text,'lxml')

data = soup.select('#main>div>div.mtop.firstMod.clearfix>div.centerBox>ul.newsList>li>a')
 

for i in data:
    result={
        'title':i.get_text(),
        'link':i.get('href')
    }
print (result)
