try:
    num = int(input("请输入一个整数"))
    resut = 8 / num
# except (ZeroDivisionError, ValueError):
#     print("除0错误")
except ValueError:
    print("格式错误")
except Exception as result:
    print("未知错误 %s" % result)
else:
    print("没有任何异常出现")
finally:
    print("这段代码必定执行")

