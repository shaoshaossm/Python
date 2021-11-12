class Tool(object):
    @staticmethod
    def run():
        print("")
    count = 0

    @classmethod
    def show_tool_class(cls):
        print("工具对象的数量 %d" % cls.count)

    def __init__(self, name):
        self.name = name
        Tool.count += 1


tool1 = Tool("斧头")
tool2 = Tool("斧头2")
Tool.show_tool_class()
