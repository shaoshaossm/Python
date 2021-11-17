# 彼岸图网美女图片
import requests
from lxml import html
import os

if __name__ == "__main__":
    if not os.path.exists('E:\\pachongzhuanyongwenjianjia\\bizhimeinv'):
        os.makedirs('E:\\pachongzhuanyongwenjianjia\\bizhimeinv')
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36'
    }
    url = "https://pic.netbian.com/4kqiche/index_%d.html"

    for pageNum in range(2, 4):
        new_url = format(url % pageNum)
        response = requests.get(url=new_url, headers=headers)
        # 手动设置相应数据的编码格式
        # response.encoding = 'utf-8'
        page_text = response.text
        tree = html.etree.HTML(page_text)
        li_list = tree.xpath('//ul[@class="clearfix"]/li')
        for li in li_list:
            img_src = "https://pic.netbian.com" + li.xpath('./a/img/@src')[0]
            img_name = li.xpath('./a/img/@alt')[0] + '.jpg'
            # 通用中文乱码的解决方案
            img_name = img_name.encode('iso-8859-1').decode('gbk')
            print(img_name, img_src)
            img_data = requests.get(url=img_src, headers=headers).content
            imgPath = 'E:\\pachongzhuanyongwenjianjia\\bizhimeinv\\' + img_name
            with open(imgPath, 'wb') as fp:
                fp.write(img_data)
                print(img_name, img_src,"下载成功")
