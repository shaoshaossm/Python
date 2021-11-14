# 爬取网站首页
import requests

if __name__ == "__main__":
    url = "https://shaoshaossm.github.io/"
    response = requests.get(url=url)
    page_text = response.text

    print(page_text)
    with open('./ssm.html', 'w', encoding='utf-8') as fp:
        fp.write(page_text)
    print("爬取结束")
