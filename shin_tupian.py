# https://www.bilibili.com/video/av75181368?from=search&seid=3279957562646786213
# 百度图片
import requests
import re

url_name = input('请输入图片类型:')
url = 'https://image.baidu.com/search/index?tn=baiduimage&word={}'.format(url_name)
html = requests.get(url).text

picture_url = re.findall('"objURL":"(.*?)"',html)

for picture_urls in picture_url:
    imget = requests.get(picture_urls).content
    name  = picture_urls.split('/')[-1]
    with open(f'{name}','wb') as f:
        f.write(imget)