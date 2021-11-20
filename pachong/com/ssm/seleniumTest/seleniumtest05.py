from selenium import webdriver
from time import sleep
# 无可视化界面
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
# 规避selenium检测
from selenium.webdriver import ChromeOptions

# 实现无可视化界面的操作
chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')

# 实现规避检测
option = ChromeOptions()
option.add_experimental_option('excludeSwitches', ['enable-automation'])

s = Service("chromedriver.exe")
driver = webdriver.Chrome(service=s)

# bro = webdriver.Chrome(executable_path='./chromedriver',options=chrome_options)
bro = webdriver.Chrome(chrome_options=chrome_options, options=option)

bro.get('https://qzone.qq.com/')
print(bro.page_source)

sleep(3)
bro.quit()
