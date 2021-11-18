# 爬取梨视频
import requests
from lxml import html
from multiprocessing.dummy import Pool

if __name__ == "__main__":
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36'
    }
    url = "https://www.pearvideo.com/category_10"

    page_text = requests.get(url=url, headers=headers).text
    tree = html.etree.HTML(page_text)
    li_list = tree.xpath('//ul[@id="listvideoListUl"]/li')
    urls = []  # 所有视频的连接
    for li in li_list:
        detail_url = 'https://www.pearvideo.com/' + li.xpath('./div/a/@href')[0]
        href = li.xpath('./div/a/@href')[0]
        name = li.xpath('./div/a/div[2]/text()')[0] + '.mp4'
        video_id = detail_url.split('_')[1]
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36'
            , 'Referer': 'https://www.pearvideo.com/' + href
        }
        video_href = 'https://www.pearvideo.com/videoStatus.jsp?contId=' + video_id
        video_url = requests.get(url=video_href, headers=headers).json()
        video = video_url["videoInfo"]["videos"]["srcUrl"]
        video = video.replace(video.split('/')[-1].split('-')[0], 'cont-%s' % video_id)
        dic = {
            'name': name,
            'url': video
        }

        urls.append(dic)
    print(urls)

    def get_video_data(dic):
        url = dic['url']
        print(dic['name'], '正在下载。。。')
        data = requests.get(url=url, headers=headers).content
        with open(dic['name'], 'wb') as fp:
            fp.write(data)
            print(dic['name'], '下载成功')


    # 使用线程池对视频数据进行请求
    pool = Pool(4)
    pool.map(get_video_data, urls)
    pool.close()
    pool.join()

