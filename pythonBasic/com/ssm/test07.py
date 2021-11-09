class Persion:
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

    def __str__(self):
        return "我的名字叫 %s 体重是 %.2f 公斤" % (self.name, self.weight)

    def run(self):
        self.weight -= 0.5

    def eat(self):
        self.weight += 1


xiaoming = Persion("小明", 75)
xiaoming.run()
xiaoming.eat()
print(xiaoming)
xiaoming = Persion("小明2", 45)
xiaoming.run()
xiaoming.eat()
print(xiaoming)
