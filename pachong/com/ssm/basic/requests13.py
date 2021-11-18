# 模拟登陆无验证码并获取用户数据
import requests
from lxml import html

if __name__ == "__main__":
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36'
    }
    session = requests.session()
    url = "https://work.shopeebao1688.com/login.html"
    page_text = requests.get(url=url, headers=headers).text
    tree = html.etree.HTML(page_text)
    login_url = "https://work.shopeebao1688.com/index/Login/doLogin?username=13668567749&password=yangbiao2021"
    data = {
        'username': '13668567749',
        'password': 'yangbiao2021'
    }
    response = session.post(url=login_url, headers=headers, data=data)
    login_page_text = response.text
    print(response.status_code)
    detail_url = "https://work.shopeebao1688.com/main"
    # 使用携带cookie 的session 进行get请求的发送
    detail_page_text = session.get(url=detail_url, headers=headers).text
    with open('xiabao.html', 'w', encoding='utf-8') as fp:
        fp.write(detail_page_text)
