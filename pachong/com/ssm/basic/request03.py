# 金山词霸
import requests
import json

if __name__ == "__main__":
    # UA伪装
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36'
    }
    url = "https://dict.iciba.com/dictionary/word/suggestion?word=dog&nums=5&ck=709a0db45332167b0e2ce1868b84773e&timestamp=1636881723426&client=6&uid=123123&key=1000006&is_need_mean=1&signature=a53fdc6d6d5fa01f307780c4b7768abc"
    # post请求参数处理
    word = input("enter a word")
    data = {
        'kw': word
    }
    # 携带参数的
    response = requests.get(url=url, params=data, headers=headers)
    dict_obj = response.json()
    print(dict_obj)
    # 持久化存储
    fileName = word+'.json'
    fp = open(fileName, 'w', encoding='utf-8')
    json.dump(dict_obj, fp, ensure_ascii=False)
    print('voer!!!')
