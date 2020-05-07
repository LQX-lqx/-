#https://www.bilibili.com/video/av45274089

# post 请求

# 1,基于控制台获取输入---待翻译的词语
# 2,设定待请求的url
# 3,建立post表单
# 4,提交post表单
# 5,接收响应结果,并解析提取
# 6,打印翻译结果
# 7.设置退出机制

import requests
import json

while True:
    # 1
    content = input('请输入:')

    # 7
    if content == '':
        print('没有有效输入')
        break

    # 2
    url = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule'
    # 3
    post_form = {
        'i': content,
        'from': 'AUTO',
        'to': 'AUTO',
        'smartresult': 'dict',
        'client': 'fanyideskweb',
        'salt': '15747502030725',
        'sign': '387f5781f5909adafae2a0e93813b177',
        'ts': '1574750203072',
        'bv': 'bc250de095a39eeec212da07435b6924',
        'doctype': 'json',
        'version': '2.1',
        'keyfrom': 'fanyi.web',
        'action': 'FY_BY_REALTlME'
    }
    # 4
    response = requests.post(url, data=post_form)
    # 5
    trans_json = response.text
    # 转换成python的字典格式
    trans_dict = json.loads(trans_json)
    # 翻译结果的索引
    result = trans_dict['translateResult'][0][0]['tgt']
    # 6
    print('翻译结果:')
    print(result)



