re = 10


def test(num):
    print("在函数内部%d 对应的内存地址是 %d" % (num, id(num)))
    result = "hello"
    print("函数要返回数据的内存地址是 %d" % id(result))
    return result
    global re

    re = 90


a = 10

print("a 变量保存数据的内存地址是 %d " % id(a))

r = test(a)

print("%s 的内存地址是 %d" % (r, id(r)))


def measure():
    a11 = 1031
    a22 = 11
    return a11, a22


s, d = measure()
print(s)
print(d)
print(measure())


def demo(num_list = True):
    num_list+=num_list
    print(num_list)


num_list = "a"
demo(num_list)
print(num_list)
