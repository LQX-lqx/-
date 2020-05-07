# https://segmentfault.com/a/1190000019078952
# 百度新闻
import re
import time
import requests
import tldextract

def save_to_db(url, html):
    # 保存网页到数据库，我们暂时用打印相关信息代替
    print('%s : %s' % (url, len(html)))

def crawl():
    # 1\. download baidu news
    hub_url = 'http://news.baidu.com/'
    res = requests.get(hub_url)
    html = res.text

    # 2\. extract news links
    ## 2.1 extract all links with 'href'
    links = re.findall(r'href=[\'"]?(.*?)[\'"\s]', html)
    print('find links:', len(links))
    news_links = []
    ## 2.2 filter non-news link
    for link in links:
        if not link.startswith('http'):
            continue
        tld = tldextract.extract(link)
        if tld.domain == 'baidu':
            continue
        news_links.append(link)

    print('find news links:', len(news_links))
    # 3\. download news and save to database
    for link in news_links:
        html = requests.get(link).text
        save_to_db(link, html)
    print('works done!')

def main():
    while 1:
        crawl()
        time.sleep(300)

if __name__ == '__main__':
    main()