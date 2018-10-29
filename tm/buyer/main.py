#-*- coding: utf-8 -*-
import random
import sys
sys.path.insert(0, '/Users/user/PycharmProjects/MakePerson/tm/general/')
import functions as fc
import accounts as ac
import codes as cd
import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.common.action_chains import ActionChains
import pandas as pd
import numpy as np




LoginUrl = "https://login.ticketmonster.co.kr/user/loginform?return_url="
ItemUrl = [
    "https://www.ticketmonster.co.kr/deal/1156912910?keyword=%EC%8B%B1%EA%B0%80%ED%8F%AC%EB%A5%B4+%EC%9C%A0%EB%8B%88%EB%B2%84%EC%85%9C%EC%8A%A4%ED%8A%9C%EB%94%94%EC%98%A4&reason=er&etype=nm&useArtistchaiRegion=Y",
    "https://www.ticketmonster.co.kr/deal/1574650942?keyword=%EC%8B%B1%EA%B0%80%ED%8F%AC%EB%A5%B4+%EC%9C%A0%EB%8B%88%EB%B2%84%EC%85%9C%EC%8A%A4%ED%8A%9C%EB%94%94%EC%98%A4&reason=er&etype=nm&useArtistchaiRegion=Y"
]


driver = webdriver.Chrome('/Users/user/PycharmProjects/MakePerson/tm/buyer/chromedriver')
timeStap = []
for Num in range(12,16,1):
    driver.get(cd.company_code['login_url'])
    fc.login(driver , ac.tm_acoountsID[Num] , ac.tm_acoountsPAW[Num])



    #첫번쨰 싱가포르 유니버셜
    driver.get(ItemUrl[0])
    fc.reservation(driver , 9)
    fc.order(driver , ac.tm_acoountsLname[Num] , ac.tm_acoountsFname[Num] , "davidkim@kimnkims.com" , str(5))
    fc.wait(driver)
    time = datetime.datetime.now()
    timeStap.append(time)
    fc.logout(driver)

print(timeStap)
