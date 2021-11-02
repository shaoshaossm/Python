import random, easygui
secret = random.randint(1,100)
guess = 0
tries = 0
easygui.msgbox("""你好 ,baby!! 让我们来玩一个猜数字的游戏.现在我心里想了一个数字.在1到100之间,你有六次尝试的机会.""")
while guess != secret and tries < 6:
    guess = easygui.integerbox("输入你猜的数字")
    if not guess:
        break
    if guess<secret:
        easygui.msgbox(str(guess) + "你猜的太小了,baby!")
    elif guess>secret:
        easygui.msgbox(str(guess) + "你猜的太大了,baby!")
        tries += 1
if guess ==secret:
    easygui.msgbox("你个垃圾终于给老子猜对了!!!")
else:
    easygui.msgbox("憨批,这都猜不对,你数学是体育老师教的吗???")