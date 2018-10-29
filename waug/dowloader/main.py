#-*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.common.action_chains import ActionChains
from bs4 import BeautifulSoup
from datetime import datetime
from requests import get
import os
import PyPDF2
import sys
sys.path.insert(0, '/Users/user/PycharmProjects/MakePerson/waug/general/')
import functions  as fc
import accounts as ac
#import codes as cd




def ticket(driver):
    # 티켓 받는 곳까지 가는 기다림
    # 마이페이지 클릭
    WebDriverWait(driver, 1000000).until(EC.presence_of_element_located(
        (By.XPATH,
         "/html/body/div[3]/header/nav/div[1]/div[3]/ul/li[4]/a/img"))).click()
    WebDriverWait(driver, 10).until(EC.presence_of_element_located(
        (By.XPATH,
         "/html/body/div[3]/header/nav/div[1]/div[3]/div/ul/li[2]/div[2]"))).click()
    time.sleep(1)
    WebDriverWait(driver, 10).until(EC.presence_of_element_located(
        (By.XPATH,
         "/html/body/main/div/div[4]/div[2]/div[2]/div/a"))).click()


downlist = ac.waug_accounts[:41]
options = webdriver.ChromeOptions()
options.add_argument("--window-size=1920,1080")
driver = webdriver.Chrome('/Users/user/PycharmProjects/MakePerson/waug/buyer/chromedriver' , options=options)
waug_HOMEPAGE = "https://www.waug.com/main"


for i in range(len(downlist)):
    #driver = webdriver.Chrome('/Users/user/PycharmProjects/buyer/chromedriver')
    driver.get(waug_HOMEPAGE)
    fc.login(driver, ac.waug_accounts[i], "tongsung8116!")
    time.sleep(1)
    driver.get("https://www.waug.com/my/order.html")

    time.sleep(2)
    driver.find_element_by_xpath(
        "//*[@id='content']/div/div/div/div[3]/div[1]/div[1]"
        ).click()
    time.sleep(1)
    driver.find_element_by_xpath(
        "//*[@id='voucher_file_down']"
    ).click()
    fc.logout(driver)





