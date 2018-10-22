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
sys.path.insert(0, '/Users/user/PycharmProjects/MakePerson/mr/general/')
#import functions  as fc
import accounts as ac
#import codes as cd


def logout(driver):
    #click the uppon img
    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH,
                                        "/html/body/div[3]/header/nav/div[1]/div[3]/ul/li[4]/a/img"
                                        ))).click()
    #click the log out btn
    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH,
                                       "/html/body/div[3]/header/nav/div[1]/div[3]/div/ul/li[5]/div"
                                       ))).click()


def download(url , file_name):
    with open(file_name, "wb")as file:
        response = get(url)
        file.write(response.content)

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


downlist = ac.MrKimnKimsAcc[46:]
driver = webdriver.Chrome('/Users/user/PycharmProjects/MakePerson/mr/downloader/chromedriver')
for i in range(len(downlist)):
    #driver = webdriver.Chrome('/Users/user/PycharmProjects/buyer/chromedriver')
    driver.get("https://www.myrealtrip.com/users/sign_in")
    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, "/html/body/main/div/div/div[3]/form/div/div[1]/div/div[2]/div/input"))).send_keys(
            downlist[i])
    driver.find_element_by_xpath( "//*/input[@name='user[password]']").send_keys("tongsung8116!")
        #driver.execute_script( "//*/input[@name='btn btn-default']")
    login_but = driver.find_element_by_xpath("/html/body/main/div/div/div[3]/form/div/div[4]/button")
    login_but.click()#로그인 버튼 클릭학

    driver.get("https://www.myrealtrip.com/traveler/reservations/ongoing")

    ticket(driver)

    time.sleep(6)

    # 티켓 html 가지고오기
    driver.implicitly_wait(10)
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')
    noti = soup.select('a.voucher-btn')

    # 바우처 리스트에 저장
    voucher_list = []
    for i in range(4):
        voucher = str(noti[i])[29:178]
        voucher_list.append(voucher)

    # clk_ticket(driver) 티켓 출력하는 함수
    now = datetime.now()
    for i in range(4):
        voucher_name = "mr" + "uss" + str(now.minute) + str(now.second) + "_" + str(i) + ".pdf"
        download(voucher_list[i], voucher_name)

        pdfFileObj = open(voucher_name, 'rb')  # 'rb' for read binary mode
        pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

        pageObj = pdfReader.getPage(0)  # '9' is the page number
        vou_reserCode = 'mr' + '_' + 'uss' + '_' + str(pageObj.extractText())[13:31] + '.pdf'
        print(vou_reserCode)

        pdfFileObj.close()

        ff = '/Users/user/PycharmProjects/MakePerson/mr/downloader/' + voucher_name
        ffr = ff.replace(voucher_name, vou_reserCode)
        os.rename(ff, ffr)
        time.sleep(5)
    # 다음 계정으로 넘어가기
    logout(driver)
    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH,
                               "/html/body/div[3]/header/nav/div[1]/div[3]/ul/li[3]/a"
                               ))).click()
    driver.refresh()