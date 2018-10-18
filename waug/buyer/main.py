#-*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.alert import Alert
import requests
import sys
sys.path.insert(0, '/Users/owner/PycharmProjects/MakePerson/waug/general/')
import functions as fc



waug_HOMEPAGE = "https://www.waug.com/main"
waug_hk_dl_ITEMURL = "https://www.waug.com/good/?idx=104500"
waug_sin_uss_ITEMURL = "https://www.waug.com/good/?idx=105851"

USER_CON = ["","Brown","Robinson","Thompson","Wright","Walker","White","Davies","Edwards"]
USER = USER_CON[7]
USERID = USER + "@poongsung.me"
PASSWORD = "tongsung8116!"
USE_DATE = str(int(time.strftime("%d"))+2)
F_NAME = USER
L_NAME = USER[0]
MD_PHONE = "7251"
LT_PHONE = "8121"




if __name__ == "__main__":
    options = webdriver.ChromeOptions()
    options.add_argument("--kiosk")
    driver = webdriver.Chrome('/Users/owner/PycharmProjects/MakePerson/waug/buyer/chromedriver' , options=options)
    driver.wait = WebDriverWait(driver, 2)

    driver.get(waug_HOMEPAGE)
    driver.wait = WebDriverWait(driver, 2)
    fc.login(driver , USER_CON[1]+"@poongsung.me" , PASSWORD )
    time.sleep(1)
    driver.get(waug_sin_uss_ITEMURL)
    #checkStock & coupon_check은 spy로
    #fc.checkStock(driver,"http://naver.com")
    #fc.coupon_check(driver)
    fc.checkOpt(driver , 1)
    fc.order(driver, 'kim' , '7251' , '8121' ,'last')
    fc.payment(driver)
    fc.eticket(driver)
    driver.wait = WebDriverWait(driver, 2)
    driver.get("https://www.waug.com/my/order.html")
    driver.wait = WebDriverWait(driver, 2)


    #i = 1
    #while(checkStock(driver, i)):
    #    i += 1
     #   time.sleep(SLEEPSEC)
      #  if (i > LOOP and LOOP != -1):
       #     break
        #driver.get(ITEMURL)

    #checkout(driver)

   # order(driver)