import asyncio


async def request(url):
    print("正在请求的url", url)
    print("请求成功", url)
    return url

# async 修饰的函数,调用之后返回的是一个协程对象
c = request('www.baidu.com')
# # 创建事件循环对象
# loop = asyncio.get_event_loop()
# # 将协程对象注册到loop中,然后启动loop
# loop.run_until_complete(c)

# task使用
#loop = asyncio.get_event_loop()


# 基于loop创建一个task对象
# task = loop.create_task(c)
#
# print(task)
# loop.run_until_complete(task)
# print(task)

# future的使用
# loop = asyncio.get_event_loop()
# task = asyncio.ensure_future(c)
# print(task)
# loop.run_until_complete(task)
# print(task)

def callback_func(task):
    print(task.result())


# 绑定回调
loop = asyncio.get_event_loop()
task = asyncio.ensure_future(c)
task.add_done_callback(callback_func)
loop.run_until_complete(task)
