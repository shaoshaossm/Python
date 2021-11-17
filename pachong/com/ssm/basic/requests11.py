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
    img_data = requests.get(url=code_img_src, headers=headers).content
    with open('./code.jpg', 'wb') as fp:
        fp.write(img_data)
    chaojiying = chaojiying.Chaojiying_Client('19858165529', 'hxl158120', '925040')  # 用户中心>>软件ID 生成一个替换 96001
    im = open('./code.jpg', 'rb').read()  # 本地图片文件路径 来替换 a.jpg 有时WIN系统须要//
    print(chaojiying.PostPic(im, 1004))  # 1902 验证码类型  官方网站>>价格体系 3.4+版 print 后要加()
