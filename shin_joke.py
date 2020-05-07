# https://www.bilibili.com/video/av45259017

# 爬笑话

import requests
from bs4 import BeautifulSoup


headers = {
"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36"
}
url = 'http://xiaodiaodaya.cn/article/view.aspx?id=6762'
res = requests.get(url,headers=headers)
res.encoding = res.apparent_encoding

dom = BeautifulSoup(res.text,features='lxml')
com = dom.select('div.content')[0].get_text()

with open('joke.txt','w',encoding='utf8') as w :
    w.write(com)

