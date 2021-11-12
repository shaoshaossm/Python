class MusicPlayer:
    def __new__(cls, *args, **kwargs):
        # 创建对象时,new 方法会被自动调用
        print("创建对象分配空间")
        # 为对象分配空间
        instance = super().__new__(cls)

        # 返回对象的调用
        return instance

    def __init__(self):
        print("音乐播放器初始化")


player = MusicPlayer()
print(player)
