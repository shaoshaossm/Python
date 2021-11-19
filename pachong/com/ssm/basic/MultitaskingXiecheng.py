import asyncio
import time


async def request(url):
    print("正在下载", url)
    # time.sleep(2)  6s
    # 当在asyncio中遇到阻塞操作必须手动挂起
    await asyncio.sleep(2)  # 2s
    print("下载完毕", url)

start = time.time()
urls = [
    'www.baidu.com',
    'www.4399.com',
    'www.ssm.com']
stasks = []
for url in urls:
    c = request(url)
    task = asyncio.ensure_future(c)
    stasks.append(task)
loop = asyncio.get_event_loop()
# 将任务列表封装到wait中
loop.run_until_complete(asyncio.wait(stasks))
print(time.time()-start)

