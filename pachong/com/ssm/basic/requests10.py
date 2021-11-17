# 全国城市列表(两种方式)
import requests
from lxml import html

if __name__ == "__main__":
    # headers = {
    #     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36'
    # }
    # url = "https://www.aqistudy.cn/historydata/"
    # page_text = requests.get(url=url, headers=headers).text
    # tree = html.etree.HTML(page_text)
    # hot_li_list = tree.xpath('//div[@class="bottom"]/ul/li')
    # hot_city_names = []
    # all_city_Names = []
    # # 解析到热门城市名称
    # for li in hot_li_list:
    #     hot_city_name = li.xpath('./a/text()')[0]
    #     hot_city_names.append(hot_city_name)
    #
    # # 解析到全部城市名称
    # city_names_list = tree.xpath('//div[@class="bottom"]/ul/div[2]/li')
    # for li in city_names_list:
    #     city_name = li.xpath('./a/text()')[0]
    #     all_city_Names.append(city_name)
    # print(hot_city_names, len(hot_city_names),  all_city_Names, len(all_city_Names))
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36'
    }
    url = "https://www.aqistudy.cn/historydata/"
    page_text = requests.get(url=url, headers=headers).text
    tree = html.etree.HTML(page_text)
    all_li_list = tree.xpath('//div[@class="bottom"]/ul/li/a | //div[@class="bottom"]/ul/div[2]/li/a')
    all_city_Names = []
    # 解析到热门城市名称
    for li in all_li_list:
        all_city_Name = li.xpath('./text()')[0]
        all_city_Names.append(all_city_Name)

    print(all_city_Names, len(all_city_Names))
