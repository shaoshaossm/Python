def say_hello(num, num2):
    """

    :param num: 数字1
    :param num2: 数字2
    :return:
    """
    result = num + num2
    return result


def say_hello2():
    row = 0
    while row < 6:
        res = say_hello(19, 10)
        print(res)
        row += 1



# print(say_hello(19, 11))
say_hello2()
