import requests
from bs4 import BeautifulSoup
htm_str_before = '''
        <!DOCTYPE html>
<html>
	<head>
		<meta charset="GBK">
		<title></title>
	</head>
	<body>
		<table>

        '''
htm_str_after='''
		</table>
	</body>
</html>
        '''
# 下载器
headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36"}

url = 'https://www.xicidaili.com/'
res = requests.get(url,headers=headers)
# print(res.text)
# 解析器
dom = BeautifulSoup(res.text,'html.parser')
con = dom.find_all('tr')
# print(con)
con=str(con)
# 缓存器
str_a=''
for i in con:
    with open('a.html','w',encoding='GBK') as e:
        str_a+=i
        total=htm_str_before+str_a+htm_str_after
        e.write(total)





