class Cat:
    def __init__(self, new_name):
        print("这是一个初始化方法")
        self.name = new_name
    def __del__(self):
        print("我去了")
    def eat(self):
        print("%s 爱吃鱼" % self.name)


tom = Cat("狸花猫")

tom.eat()
print(tom.name)
