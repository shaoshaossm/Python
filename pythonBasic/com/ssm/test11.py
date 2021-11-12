def demo1():
    return int(input("请输入一个整数"))


def demo2():
    demo1()


try:
    print(demo2())
except Exception as result:
    print(result)
