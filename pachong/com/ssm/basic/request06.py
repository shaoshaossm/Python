# 爬取糗事百科图片--分页爬取
import requests
import re
import os

requests.packages.urllib3.disable_warnings()
if __name__ == "__main__":
    if not os.path.exists('E:\\pachongzhuanyongwenjianjia\\qiutu'):
        os.makedirs('E:\\pachongzhuanyongwenjianjia\\qiutu')
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36'
    }
    # 设置一个通用的url模板
    url = "https://www.qiushibaike.com/imgrank/page/%d/"

    for pageNum in range(1, 6):
        new_url = format(url % pageNum)

        # 二进制形式的图片数据
        page_text = requests.get(url=new_url, headers=headers).text
        ex = '<div class="thumb">.*?<img src="(.*?)" alt.*?</div>'
        img_src_list = re.findall(ex, page_text, re.S)
        for src in img_src_list:
            # 拼接出一个完整的图片地址
            src = 'https:' + src
            # 请求图片二进制数据
            img_data = requests.get(url=src, headers=headers).content
            # 生成图片名称
            img_name = src.split('/')[-1]
            # 图片存储路路径
            imgPath = 'E:\\pachongzhuanyongwenjianjia\\qiutu\\' + img_name
            with open(imgPath, 'wb') as fp:
                fp.write(img_data)
                print(img_name, "下载成功")
