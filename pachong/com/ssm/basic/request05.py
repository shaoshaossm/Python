# 药监总局化妆品生产许可
import requests
import json

if __name__ == "__main__":
    # UA伪装
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36'
    }
    id_list = []
    all_data_list = []
    url = "http://scxk.nmpa.gov.cn:81/xk/itownet/portalAction.do?method=getXkzsList"
    # post请求参数处理
    for page in range(1, 6):
        page = str(page)
        data = {
            'on': 'true',
            'page': page,
            'pageSize': '15',
            'productName': '',
            'conditionType': '1',
            'applyname': '',
            'applysn': '',
        }
        # 携带参数的

        json_ids = requests.post(url=url, headers=headers, data=data).json()
        for dic in json_ids['list']:
            id_list.append(dic['ID'])

    post_url = "http://scxk.nmpa.gov.cn:81/xk/itownet/portalAction.do?method=getXkzsById"
    for id in id_list:
        data = {
            'id': id
        }
        detail_json = requests.post(url=post_url, headers=headers, data=data).json()
        print(detail_json)
        all_data_list.append(detail_json)
    # 持久化存储
    fp = open('./allData.json', 'w', encoding='utf-8')
    json.dump(all_data_list, fp=fp, ensure_ascii=False)
    print('voer!!!')
