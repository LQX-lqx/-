# 爬猫眼电影名字

import requests
from bs4 import BeautifulSoup
import agent_name
import random
headers = {
    'User-Agent':random.choice(agent_name.my_chrome_agent)
}
url = 'https://maoyan.com/board/4'
res = requests.get(url,headers=headers)
res.encoding = 'utf-8'
# print(res.text)
dom = BeautifulSoup(res.text,'html.parser')
cod = dom.select('.name')
# print(cod)
for i in cod:

# 第一种方法
    print(i.text.strip())

# 第二种方法
    # a =i.text.strip()+'\n'
    # b =  str(a)
    # with open('d.txt','a+',encoding='utf-8') as e:
    #     e.write(b)


