#-*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.alert import Alert
import requests
from general import functions as fc
import sys
sys.setdefaultencoding('utf-8')


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
    driver = webdriver.Firefox()
    driver.wait = WebDriverWait(driver, 2)

    driver.get(waug_HOMEPAGE)
    driver.wait = WebDriverWait(driver, 2)
    fc.login(driver)
    driver.get(waug_sin_uss_ITEMURL)
    checkStock(driver)
    coupon_check(driver)
    checkOpt(driver)
    order(driver)
    payment(driver)
    eticket(driver)
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