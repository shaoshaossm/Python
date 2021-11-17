# 58二手房
import requests
from lxml import html

if __name__ == "__main__":
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36'
    }
    url = "https://jh.58.com/ershoufang/?PGTID=0d100000-0021-389e-914e-5d1b7be3c806&ClickID=2"
    page_text = requests.get(url=url, headers=headers).text
    tree = html.etree.HTML(page_text)
    div_list = tree.xpath(
        # '/html/body/div[1]/div/div/section/section[3]/section[1]/section[2]/div')
        # '//section[@class="list-body"]/section[3]/section[1]/section[2]/div')
        '//section[@class="list"]/div')
    print(div_list)
    for div in div_list:
        title = div.xpath('./a/div[2] / div[1] / div[1] / h3 / text()')
        fp = open('58.txt', 'a', encoding='utf-8')
        print(title)
        fp.write(str(title) + '\n')
