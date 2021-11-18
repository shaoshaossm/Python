# 验证码
import requests
from lxml import html

import chaojiying

# 封装识别验证码函数


if __name__ == "__main__":
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36'
    }
    url = "https://so.gushiwen.cn/user/login.aspx?from=http://so.gushiwen.cn/user/collect.aspx"
    page_text = requests.get(url=url, headers=headers).text
    tree = html.etree.HTML(page_text)
    code_img_src = 'https://so.gushiwen.cn/' + tree.xpath('//*[@id="imgCode"]/@src')[0]

    print(code_img_src)
    code_img_data = requests.get(url=code_img_src, headers=headers).content
    with open('./code.jpg', 'wb') as fp:
        fp.write(code_img_data)
    chaojiying = chaojiying.Chaojiying_Client('19858165529', 'hxl158120', '925040')  # 用户中心>>软件ID 生成一个替换 96001
    im = open('./code.jpg', 'rb').read()  # 本地图片文件路径 来替换 a.jpg 有时WIN系统须要//
    code = chaojiying.PostPic(im, 1004)
    code_img = code['pic_str']
    print(code_img)  # 1902 验证码类型  官方网站>>价格体系 3.4+版 print 后要加()
    # 模拟登陆
    login_url = "https://so.gushiwen.cn/user/login.aspx?"
    data = {
        'from': 'http://so.gushiwen.cn/user/collect.aspx',
        'email': '19858165529',
        'pwd': 'hxl158120',
        'code': code_img,
        'denglu': '登录',
    }
    response = requests.post(url=login_url, headers=headers, data=data)
    login_page_text = response.text
    print(response.status_code)

    with open('changyan.html', 'w', encoding='utf-8') as fp:
        fp.write(login_page_text)
