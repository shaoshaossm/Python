class Gun:
    def __init__(self, model):
        # 枪支模型
        self.model = model
        # 子弹数量
        self.bullet_count = 0

    def add_bullet(self, count):
        self.bullet_count += count

    def shoot(self):
        if self.bullet_count <= 0:
            print("[%s 没有子弹了]" % self.model)
            return
        self.bullet_count -= 1
        print("%s 发射子弹成功 剩余 %d 子弹" % (self.model, self.bullet_count))


class Soldier:
    def __init__(self, name):
        self.name = name
        self.gun = None

    def fire(self):
        if self.gun is None:
            print("[%s] 没有抢" % self.name)
            return
        print("冲啊...[%s]" % self.name)
        self.gun.add_bullet(50)
        self.gun.shoot()


ak47 = Gun("ak47")
xsd = Soldier("许三多")
xsd.gun = ak47
xsd.fire()

