# 爬取糗事百科指定图片
import requests

requests.packages.urllib3.disable_warnings()
if __name__ == "__main__":
    url = "https://pic.qiushibaike.com/article/image/JMR6TS435AHM1ZCY.jpg"
    # 二进制形式的图片数据
    img_data = requests.get(url=url, ).content
    with open('./qiutu.jpg', 'wb') as fp:
        fp.write(img_data)
