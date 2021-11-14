# 网页采集器
import requests
if __name__ == "__main__":
    # UA伪装
    headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36'
    }
    url = "https://www.baidu.com/s"
    # 处理url携带参数
    kw = input('enter a word：')
    param  = {
        'wd':kw
    }
    # 携带参数的
    response = requests.get(url=url,params=param,headers=headers)

    page_text = response.text
    fileName = kw+'.html'
    with open(fileName, 'w', encoding='utf-8') as fp:
        fp.write(page_text)
    print(fileName,"保存成功！！！")