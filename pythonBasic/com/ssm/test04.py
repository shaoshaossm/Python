str = "   h e ll "
for s in str:
    print(s ,end="")
print()
print (str.strip())

str = "000000032\t10\tRu\tnoob\t01230000000"
print (str.strip('0'))  # 去除首尾字符 0

str2 = "   Runoob      ";  # 去除首尾空格
print(str2)
print (str2.strip())
print(str.split())