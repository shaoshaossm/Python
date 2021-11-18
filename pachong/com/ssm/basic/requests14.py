# 代理服务器
import requests

url = "https://www.baidu.com/s?ie=UTF-8&wd=ip"
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36'
}
page_text = requests.get(url=url, headers=headers, proxies={"HTTP": '39.99.149.148'}).text
with open('ip2.html', 'w', encoding='utf-8') as fp:
    fp.write(page_text)
