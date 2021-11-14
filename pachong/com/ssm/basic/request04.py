# 豆瓣高分电影
# 网页采集器
import requests
import json

if __name__ == "__main__":
    # UA伪装
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36'
    }
    url = "https://movie.douban.com/j/search_subjects?"
    param = {
        'type': 'movie',
        'tag': '热门',
        'sort': 'recommend',
        'page_limit': '20',
        'page_start': '0'
    }

    # post请求参数处理

    # 携带参数的
    response = requests.get(url=url, params=param, headers=headers)
    list_data = response.json()
    print(list_data)
    # 持久化存储
    fp = open('./douban.json', 'w', encoding='utf-8')
    json.dump(list_data, fp, ensure_ascii=False)
    print('voer!!!')
