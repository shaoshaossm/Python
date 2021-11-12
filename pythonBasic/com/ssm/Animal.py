class Animal:
    def run(self):
        print("跑步")

    def eat(self):
        print("吃饭")


class Dog(Animal):
    def bark(self):
        print("汪汪")


geidi = Dog()
geidi.bark()
geidi.eat()
