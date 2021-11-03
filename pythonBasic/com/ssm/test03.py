names = ["zhangsan", "lisi", "wangwu"]
print(names)
names.append("zhoaliu")
print(names)
print(names.index("lisi"))
names[1] = "胡鑫亮"
print(names)
names.insert(1, "hu")
print(names)
temp = []
temp.extend(names)
print(temp)
tuple1 = (1, 2, "d", True, 2)
print(tuple1)
print(len(tuple1))
print(tuple1.index(2))

xiaoming = {"name": "小明",
            "age": 18,
            "height": 1.72}
print(xiaoming["name"])
xiaoming["weight"] = 50
xiaoming["weight"] = 45
xiaoming.pop("name")
print(xiaoming)
print("--------")
for k in xiaoming:
    print("%s - %s" % (k, xiaoming[k]))

card = [{"name": "小胡",
         "age": 18},
        {"name": "小张",
         "age": 19}]
for ren in card:
    print(ren)
