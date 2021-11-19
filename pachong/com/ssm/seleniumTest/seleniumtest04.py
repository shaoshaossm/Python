from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

bro = webdriver.Chrome(executable_path='./chromedriver')

bro.get('https://qzone.qq.com/')
# 如果定位的标签在iframe标签中，需如下操作
bro.switch_to.frame('login_frame')  # 切换浏览器标签的作用域

a_tag = bro.find_element(By.ID, 'switcher_plogin')
a_tag.click()
username_tag = bro.find_element(By.ID, 'u')
password_tag = bro.find_element(By.ID, 'p')
sleep(1)
username_tag.send_keys('')
sleep(1)
password_tag.send_keys('')
sleep(1)
btn = bro.find_element(By.ID, 'login_button')
btn.click()
sleep(3)
qiandao = bro.find_element(By.ID, 'checkin_button')
qiandao.click()
bro.switch_to.frame('checkin_likeTipsFrame')

qiandao_img = bro.find_element(By.CLASS_NAME, 'detail-box')
qiandao_img.click()
fabu = bro.find_element(By.CLASS_NAME, 'btn-submit')
fabu.click()
sleep(10)
bro.quit()

