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
sys.path.insert(0, '/Users/user/PycharmProjects/MakePerson/waug/general/')
import functions as fc
import codes as cd
import accounts as ac
import datetime

waug_HOMEPAGE = "https://www.waug.com/main"
waug_hk_dl_ITEMURL = "https://www.waug.com/good/?idx=104500"
waug_sin_uss_ITEMURL = "https://www.waug.com/good/?idx=102845"
ResulComp = cd.company_code
#ResulComp['login_url'] #hompage
#ResulComp['item_url_hk'] #hkd
#ResulComp['item_url_uss'] #uss

#ac.waug_accounts #이름 + 주소
#ac.waug_users #이름
#ac.waug_domain #이메일




if __name__ == "__main__":
    Nubers = input("how many tickets")
    StartPoint = input("What accounts do you want to start")
    options = webdriver.ChromeOptions()
    options.add_argument("--window-size=1920,1080")
    driver = webdriver.Chrome('/Users/user/PycharmProjects/MakePerson/waug/buyer/chromedriver' , options=options)



    timeStap = []
    for Nub in range(int(StartPoint),int(Nubers)+int(StartPoint),1):
        driver.get(waug_HOMEPAGE)
        fc.login(driver , ac.waug_accounts[Nub] , "tongsung8116!" )
        time.sleep(1)
        driver.wait = WebDriverWait(driver, 2)
        driver.get(waug_sin_uss_ITEMURL)
        fc.reservation(driver ,  1)
        fc.order(driver, ac.waug_users[Nub] , '7251' , '8121' ,ac.waug_users[Nub][0])
        fc.payment(driver)
        fc.eticket(driver)
        driver.get("https://www.waug.com/my/order.html")
        fc.logout(driver)
        times = datetime.datetime.now()
        timeStap.append(time)


    print(timeStap)



