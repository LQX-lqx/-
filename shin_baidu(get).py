#https://www.bilibili.com/video/av45262171

import requests
from bs4 import BeautifulSoup

# 1,网页的请求抓取
# 2,查看响应的全部内容
# 3,查看响应的具体属性

url = 'https://www.baidu.com/'
res = requests.get(url)
# res.encoding = 'utf-8'
res.encoding = res.apparent_encoding

print(type(res.text))
print(res.text)
print('------------')
print(type(res.content))
print(res.content)

# 头部文件的属性
print(res.headers)
# 状态码 属性
print(res.status_code)
# cookies 属性
print(res.cookies)