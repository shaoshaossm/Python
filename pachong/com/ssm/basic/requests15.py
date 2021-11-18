# 线程池基本使用
import requests
import time
from multiprocessing.dummy import Pool

start_time = time.time()


def get_page(str):
    print("正在下载：", str)
    time.sleep(2)
    print('下载成功', str)


name_list = ['aa', 'vv', 'cc', 'dd']
pool = Pool(4)
pool.map(get_page, name_list)
edn_time = time.time()
print(edn_time - start_time)
