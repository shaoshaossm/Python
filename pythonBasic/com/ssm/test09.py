class Dog:
    def __init__(self, name):
        self.name = name
        self.__age = 18

    def game(self):
        print("%s 蹦跳玩" % self.name)


class XiaoTianDog(Dog):
    def game(self):
        print("%s 边飞边蹦跳玩" % self.name)
    


class Person:
    def __init__(self, name):
        self.name = name

    def game_width_dog(self, dog):
        print("%s 与 %s 一起玩耍" % (self.name, dog.name))
        dog.game()


xiaoming = Person("小明")
xiaotianquan = XiaoTianDog("哮天犬")
xiaoming.game_width_dog(xiaotianquan)
wangcai = Dog("旺财")
xiaoming.game_width_dog(wangcai)
