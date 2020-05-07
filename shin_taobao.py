import requests
import json
import os
def get_pic_url(num):
    pic_url= []
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36'}
    for i in range(num):

        page_url = 'https://image.baidu.com/search/acjson?tn=resultjson_com&ipn=rj&ct=201326592&is=&fp=result&queryWord=%E5%9B%BE%E7%89%87&cl=2&lm=-1&ie=utf-8&oe=utf-8&adpicid=&st=-1&z=&ic=0&hd=&latest=&copyright=&word=%E5%9B%BE%E7%89%87&s=&se=&tab=&width=&height=&face=0&istype=2&qc=&nc=1&fr=&expermode=&force=&pn={}&rn=30&gsm=1e&1561022599290='.format(30*i)
        r = requests.get(page_url, headers=headers).text
        res = json.loads(r)['data']
        if res:
            print(res)
            for j in res:
                try:
                    url = j['hoverURL']
                    pic_url.append(url)
                except:
                    print('该图片的url不存在')

    print(len(pic_url))
    return pic_url

def down_img(num):
    pic_url  =get_pic_url(num)

    if os.path.exists('D:\图片'):
        pass
    else:
        os.makedirs('D:\图片')

    path = 'D:\图片\\'
    for index,i in enumerate(pic_url):
        filename = path +   str(index) + '.jpg'
        print(filename)
        with open(filename, 'wb+') as f:
            f.write(requests.get(i).content)
if __name__ == '__main__':
    num = int(input('爬取几次图片：一次30张'))
    down_img(num)




