from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By

bro = webdriver.Chrome(executable_path='./chromedriver')
bro.get('https://lol.qq.com/main.shtml')
# 获取浏览器当前页面的页面源码数据
bro.execute_script('window.scrollTo(0,document.body.scrollHeight)')
sleep(2)
search_btn=bro.find_element(By.ID,'J_headSearchBtn')

# search_btn = bro.find_element_by_id('J_headSearchBtn')
search_btn.click()
search_input = bro.find_element_by_id('J_hoverSearchInput')
search_input.send_keys('无限火力')
btn = bro.find_element_by_id('J_hoverSearchBtn')
btn.click()
bro.get('https://www.4399.com')
sleep(3)

bro.back()
sleep(3)
bro.forward()
sleep(5)
bro.quit()









