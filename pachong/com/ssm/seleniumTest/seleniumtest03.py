from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

bro = webdriver.Chrome(executable_path='./chromedriver')

bro.get('https://www.runoob.com/try/try.php?filename=jqueryui-api-droppable')
# 如果定位的标签在iframe标签中，需如下操作
bro.switch_to.frame('iframeResult')  # 切换浏览器标签的作用域
div = bro.find_element(By.ID, 'draggable')
# 动作链
action = ActionChains(bro)
# 点击长按指定的标签
action.click_and_hold(div)
for i in range(13):
    # (x,y) x: 水平 y： 竖直
    action.move_by_offset(17, 0).perform()
    sleep(0.3)
# 释放动作链
action.release()
sleep(5)
bro.quit()
