def show_meaus():
    print("*" * 50)
    print("欢迎使用 [名片管理系统]\n")
    print("1. 新增名片")
    print("2. 显示全部")
    print("3. 搜索名片")
    print("0. 退出系统")

    print("*" * 50)


card_list = []


def new_card():
    """新增名片"""
    name = input("请输入姓名")
    phone = input("请输入电话")
    age = input("请输入年龄")
    email = input("请输入邮箱")
    card_dict = {"name": name,
                 "phone": phone,
                 "age": age,
                 "email": email}
    card_list.append(card_dict)
    print(card_list)
    print("添加 %s 名片成功" % name)


def show_all():
    """显示全部"""
    for card_all_list in card_list:
        print(card_all_list)


def search_card():
    """搜索名片"""
    findname = input("请输入您要查找的名片名称")
    for card_all_list in card_list:
        if card_all_list["name"] == findname:
            print("%s 的信息如下:" % card_all_list["name"])
            print("%s\t%s\t%s\t%s\t" % (card_all_list["name"],
                                        card_all_list["phone"],
                                        card_all_list["email"],
                                        card_all_list["age"]))
            deal_card(card_all_list)
            break
        elif findname not in card_all_list:
            print("%s 没有找到哦" % findname)
        else:
            print("出错啦!")
            break


def deal_card(find_dict):
    """
    处理查找到的名片
    :param find_dict:查找到的名片
    """
    print(find_dict)
    action_str = input("请选择要执行的操作 1.修改 2.删除 0.返回上级菜单")
    if action_str == "1":
        find_dict["name"] = input_card_info(find_dict["name"], "姓名:")
        find_dict["phone"] = input_card_info(find_dict["phone"], "电话:")
        find_dict["email"] = input_card_info(find_dict["email"], "邮箱:")
        find_dict["age"] = input_card_info(find_dict["age"], "年龄:")

    elif action_str == "2":
        card_list.remove(find_dict)


def input_card_info(dict_value, tip_message):
    """

    :param dict_value: 字典中原有的值
    :param tip_message: 提示输入的文字
    :return: 如果输入了内容,返回内容;否则返回原有的值
    """
    result_str = input(tip_message)
    if len(result_str) > 0:
        return result_str
    else:
        return dict_value
