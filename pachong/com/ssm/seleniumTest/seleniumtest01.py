from selenium import webdriver
from lxml import html
from time import sleep
bro = webdriver.Chrome(executable_path='./chromedriver')
bro.get('http://scxk.nmpa.gov.cn:81/xk/')
# 获取浏览器当前页面的页面源码数据
page_text = bro.page_source
tree = html.etree.HTML(page_text)

li_list = tree.xpath('//ul[@id="gzlist"]/li')
for li in li_list:
    name = li.xpath('./dl/@title')[0]
    print(name)
sleep(4)
bro.quit()









