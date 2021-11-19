import asyncio
import time
import aiohttp

urls = [
    'http://127.0.0.1:5000/ssm', 'http://127.0.0.1:5000/shao', 'http://127.0.0.1:5000/hxl'
]

start = time.time()


async def get_page(url):
    async with aiohttp.ClientSession() as session:
        # headers params/data proxy='http://ip:port'
        async with await session.get(url) as response:
            page_text = await response.text()
            print(page_text)
    print('正在下载', url)
    print('下载完毕', url)


tasks = []
for url in urls:
    c = get_page(url)
    task = asyncio.ensure_future(c)
    tasks.append(task)

loop = asyncio.get_event_loop()
# 将任务列表封装到wait中
loop.run_until_complete(asyncio.wait(tasks))
print(time.time() - start)
