# 验证码模拟登陆
from selenium import webdriver
import time
import chaojiying
from PIL import Image
from selenium.webdriver.common.by import By

# 封装识别验证码函数


if __name__ == "__main__":
    bro = webdriver.Chrome(executable_path='./chromedriver')
    bro.maximize_window()
    bro.get("http://changyan.kuaizhan.com/")
    time.sleep(1)

    # tanchuangguanbi = bro.find_element(By.CLASS_NAME, ' icon-raw-error ')
    tanchuangguanbi = bro.find_element_by_class_name('icon-raw-error ')
    tanchuangguanbi.click()
    time.sleep(1)

    btn = bro.find_element_by_class_name('c-button')
    btn.click()
    time.sleep(2)
    bro.save_screenshot('aa.png')
    code_img_ele = bro.find_element_by_xpath('//*[@id="vcode-img"]')
    # 获取验证码
    # 验证码左上角坐标x，y
    location = code_img_ele.location
    print('location: ', location)
    # 验证码对应的长宽
    size = code_img_ele.size
    print('size', size)
    rangle = (
        int(location['x'])*1.25,int(location['y'])*1.25,int((location['x']) + size['width'])*1.25,int((location['y']) + size['height'])*1.25
    )
    print(rangle)
    i = Image.open('./aa.png')
    code_img_name = './code.png'
    frame = i.crop(rangle)
    frame.save(code_img_name)
    # 解析验证码
    chaojiying = chaojiying.Chaojiying_Client('19858165529', 'hxl158120', '925040')  # 用户中心>>软件ID 生成一个替换 96001
    im = open('./code.png', 'rb').read()  # 本地图片文件路径 来替换 a.jpg 有时WIN系统须要//
    code = chaojiying.PostPic(im, 1004)
    code_img = code['pic_str']
    print(code_img)  # 1902 验证码类型  官方网站>>价格体系 3.4+版 print 后要加()
    username_tag = bro.find_element(By.ID, 'normal_login_name')
    username_tag.send_keys('19858165529')
    time.sleep(2)
    password_tag = bro.find_element(By.ID, 'normal_login_password')
    password_tag.send_keys('hxl158120')
    time.sleep(2)
    text = bro.find_element_by_id('normal_login_vcode').text
    print(text)
    # fullXpath 相对路径定位不到
    Verification_code = bro.find_element(By.XPATH,'/html/body/div/div/div[4]/div[2]/div[2]/form/div[3]/div/div/div/div/div[1]/input')
    Verification_code.send_keys(code_img)
    time.sleep(2)
    Login_btn = bro.find_element_by_class_name('login-form-button')
    Login_btn.click()
    time.sleep(50)
