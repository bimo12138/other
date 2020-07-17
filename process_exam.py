# -*- coding: utf-8 -*-
"""
    Created on Tue Sep  3 19:50:44 2019
    @author: 13716
    @version: 2.0.0 U
    
    #NOTE:
        2.0.0 
        1. 添加 orc 在线识别
        2. 能够使用自动输入，修复了v1中密码无法输入的bug
        3. 开启时间检测
        
"""

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from aip import AipOcr
import time


start_time = int(time.time())

APP_ID = "10817185"
API_KEY = "yuutxCANdmgqegYwbnGHIwH3"
SECRET_KEY = "wNOvdh7WD7naZORf5alxiEXZeZaoh7X6 "

client = AipOcr(APP_ID, API_KEY, SECRET_KEY)
IMAGE_NAME = "code.png"
CODE_ERROR = "验证码错误！\n登录失败！"

def analyse_code(image):
    f = open(image, "rb")
    img = f.read()
    f.close()
    options = {}
    options["language_type"] = "ENG"
    result = client.basicGeneral(img, options=options)["words_result"][0]["words"]
    if len(result) == 4:
        return result
    else:
        return analyse_code(image)
        
username = "174003031014"
password = "liuying@"

driver = webdriver.Chrome()
driver.get("http://jwgl.lpssy.edu.cn/Jwweb/home.aspx")

all_window = driver.window_handles
now = driver.current_window_handle
all_window.remove(now)
driver.switch_to_window(all_window[0])
driver.close()
driver.switch_to_window(now)

driver.switch_to_frame("frm_login")

driver.find_element_by_id("txt_asmcdefsddsd").send_keys(username)

while driver.current_url == "http://jwgl.lpssy.edu.cn/Jwweb/home.aspx":
    
    driver.find_element_by_id("txt_psasas").click()
    driver.find_element_by_id('txt_pewerwedsdfsdff').send_keys(password)
    code = driver.find_element_by_id("txt_sdertfgsadscxcadsads")
    
    code.click()
    img = driver.find_element_by_id("imgCode")
    img.screenshot(IMAGE_NAME)
    result = analyse_code(IMAGE_NAME)
    code.send_keys(result)
    driver.find_element_by_id("btn_login").click()
    

time.sleep(2)
driver.switch_to_frame("frmbody")

driver.find_element_by_id("memuBarText9").click()
driver.find_element_by_xpath("/html/body/form/table/tbody/tr/td[1]/div/table/tbody/tr[21]/td/table/tbody/tr[3]/td[2]/span").click()
driver.switch_to_frame("frmMain")
import time
time.sleep(3)
driver.switch_to_frame("main")
all_b = driver.find_elements_by_tag_name("tr")
base_handler = driver.window_handles
url_list = []

for i in range(1, len(all_b)):
    link_a = "pj" + str(i)
    a = driver.find_element_by_id(link_a).find_element_by_tag_name('a').get_attribute("onclick")
    url = 'http://jwgl.lpssy.edu.cn/Jwweb/jxkp/' + a[17:-50]
    url_list.append(url)
    

for url in url_list:
    driver.get(url)
    all_c = driver.find_elements_by_tag_name("tr")
    if len(all_c) == 1:
        continue
    for k in range(20):
        base_name = "sel_score" + str(k)
        driver.find_element_by_id(base_name).find_element_by_tag_name("input").click()
        
    driver.find_element_by_name("Submit").click()
    driver.switch_to_alert().accept()

driver.get("http://jwgl.lpssy.edu.cn/Jwweb/MAINFRM.aspx")
time.sleep(1)
driver.switch_to_frame("frmbody")

driver.find_element_by_id("memuBarText9").click()
driver.find_element_by_xpath("/html/body/form/table/tbody/tr/td[1]/div/table/tbody/tr[21]/td/table/tbody/tr[4]/td[2]/span").click()
driver.switch_to_frame("frmMain")

import re
def get_score(text):
    return re.findall(r"最高分值为\((.*?)\.00分\)", text)[0]

time.sleep(3)
driver.switch_to_frame("main")
all_b = driver.find_elements_by_tag_name("tr")
base_handler = driver.window_handles
url_list = []
for i in range(1, len(all_b)):
    link_a = "pj" + str(i)
    a = driver.find_element_by_id(link_a).find_element_by_tag_name('a').get_attribute("onclick")
    url = 'http://jwgl.lpssy.edu.cn/Jwweb/jxkp/' + a[17:-50]
    url_list.append(url)
    
for url in url_list:
    driver.get(url)

    all_c = driver.find_elements_by_tag_name("tr")
    for k in range(6):
        base_name = "sel_score" + str(k)
        td_name = driver.find_element_by_id(base_name)
        input_name = "sel_scorecj" + str(k)
        driver.find_element_by_id(input_name).send_keys(get_score(td_name.text))
    driver.find_element_by_name("Submit").click()
    driver.switch_to_alert().accept()
driver.close()

end_time = int(time.time())
cost_time = end_time - start_time

print("评教已经结束，感谢您的使用！")

print("耗时: " + str(cost_time) + "s")
