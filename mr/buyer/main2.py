#-*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.common.action_chains import ActionChains
import sys
sys.path.insert(0, '/Users/owner/PycharmProjects/MakePerson/mr/general/')
import functions  as fc
import accounts as ac
import codes as cd
from bs4 import BeautifulSoup
from datetime import datetime
from requests import get
import sys
import pandas as pd
import numpy as np


#could not be scrolled into view
#url : https://stackoverflow.com/questions/41744368/scrolling-to-element-using-webdriver/41744591
WAITTIME = 500
SLEEPSEC = 5
LOOP = 3 # -1 for infinite

#ipacktour : http://ipacktour.com
myreal_HOMEPAGE = "https://www.myrealtrip.com/users/sign_in"
myreal_ITEMURL = ["https://www.myrealtrip.com/offers/15441","https://www.myrealtrip.com/offers/21988"]

#waug : https://www.waug.com/main/
#ipack_HOMEPAGE = "http://ipacktour.com/user/login"
#ipack_ITEMURL = "http://ipacktour.com/product/detail/view/2018042600002"


def login(driver):
    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, "/html/body/main/div/div/div[3]/form/div/div[1]/div/div[2]/div/input"))).send_keys(
        USERID)
    driver.find_element_by_xpath( "//*/input[@name='user[password]']").send_keys(PASSWORD)
    #driver.execute_script( "//*/input[@name='btn btn-default']")
    login_but = driver.find_element_by_xpath("/html/body/main/div/div/div[3]/form/div/div[4]/button")
    login_but.click()#로그인 버튼 클릭학
    #WebDriverWait(driver, WAITTIME).until(
     #   EC.presence_of_element_located((By.XPATH, "//a[@href='http://ipacktour.com/user/logout']")))

def logout(driver):
    #click the uppon img
    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH,
                                        "/html/body/div[3]/header/nav/div[1]/div[3]/ul/li[4]/a/img"
                                        ))).click()
    #click the log out btn
    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH,
                                       "/html/body/div[3]/header/nav/div[1]/div[3]/div/ul/li[5]/div"
                                       ))).click()




def checkOpt(driver):
    #상품날짜 설정 버튼 클릭
    WebDriverWait(driver, 100).until(EC.presence_of_element_located(
        (By.XPATH, "//*[@id='calendarBtn']"))).click()
    #driver.find_element_by_xpath("//*[@id='calendarBtn']").click()
    #상품날짜 선택
    WebDriverWait(driver, 100).until(EC.presence_of_element_located(
        (By.LINK_TEXT, str(rsv_date)))).click()


def checkOpt_qut(driver):
    driver.implicitly_wait(1000)
    driver.set_script_timeout(50)

    felement = driver.find_element_by_xpath(
        "//*[@id='optionBtn']/div[3]"
    )

    actions = ActionChains(driver)
    actions.move_to_element(felement).perform()

    driver.implicitly_wait(1000)
    driver.set_script_timeout(50)

    element = driver.find_element_by_xpath(
        "//*[@id='optionBtn']/div[4]/div/div/div[2]/div/div/div/span[4]/button"
    )

    actions = ActionChains(driver).click()
    actions.move_to_element(element).perform()

    i = 0
    while i < 4:
        element.click()
        i += 1
    # driver.execute_script("arguments[0].scrollIntoView();", element)

    # driver.set_script_timeout(2)
    WebDriverWait(driver, 100).until(EC.presence_of_element_located((
        By.XPATH, "//*[@id='checkPriceBtn']/button"
    ))).click()

    # driver.implicitly_wait(1000)
    # driver.set_script_timeout(50)
    time.sleep(1)
    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH,
                                                                   "/html/body/main/section/div[2]/div[1]/div[2]/div[3]/div/div[2]/form/div[2]/div/div[2]/button"
                                                                   ))).click()

#현재 안쓰는 함수
def checkout(driver):
    #update the prices
    driver.find_element_by_xpath("//*[@id='checkPriceBtn']/button").click()
    #purchase btn
    #WebDriverWait(driver, 2)
    driver.implicitly_wait(10)
    driver.execute_script("window.scrollTo(0, 500)")
    buy_btn = driver.find_element_by_xpath("/html/body/main/section/div[2]/div[1]/div[2]/div[3]/div/div[2]/form/div[2]/div/div[2]/button")
    actions = ActionChains(driver)
    actions.move_to_element(buy_btn).click()
    #WebDriverWait(driver, 20).until(
    #    EC.presence_of_element_located((By.XPATH, "/html/body/main/section/div[2]/div[1]/div[2]/div[3]/div/div[2]/form/div[2]/div/div[2]/button/span/img"))).click()
    #WebDriverWait(driver, 0).until(
     #EC.presence_of_element_located((By.LINK_TEXT, "구매하기"))).click()
    #driver.find_element_by_css_selector(".reserve-btn .button:nth-child(1)").click()

#현재 안쓰는 함수

def order(driver):
    WebDriverWait(driver, 100).until(EC.presence_of_element_located((By.XPATH,"/html/body/main/section/div/form/div[2]/div[1]/div[2]/div/div[2]/div[2]/input"))).send_keys(L_NAME)
    driver.find_element_by_xpath("/html/body/main/section/div/form/div[2]/div[1]/div[2]/div/div[3]/div[2]/input").send_keys(F_NAME)
    driver.find_element_by_xpath("/html/body/main/section/div/form/div[2]/div[1]/div[2]/div/div[4]/div[2]/input").send_keys(FULL_NAME)
    driver.find_element_by_xpath("//*[@id='input-icc']").click()
    driver.find_element_by_xpath("/html/body/main/section/div/form/div[2]/div[1]/div[2]/div/div[5]/div[2]/select/option[2]").click()
    driver.find_element_by_xpath("/html/body/main/section/div/form/div[2]/div[1]/div[2]/div/div[6]/div[2]/input").send_keys(BIRTH_DATE)
    driver.find_element_by_xpath("/html/body/main/section/div/form/div[2]/div[2]/div[2]/div/div[1]/div[2]/div[2]/input").send_keys(PHONE_NB)
    driver.find_element_by_xpath("/html/body/main/section/div/form/div[2]/div[2]/div[2]/div/div[2]/div[2]/div/select").click()
    driver.find_element_by_xpath("/html/body/main/section/div/form/div[2]/div[2]/div[2]/div/div[2]/div[2]/div/select/option[5]").click()
    driver.find_element_by_xpath("/html/body/main/section/div/form/div[2]/div[2]/div[2]/div/div[2]/div[3]/div/select").click()
    driver.find_element_by_xpath("/html/body/main/section/div/form/div[2]/div[2]/div[2]/div/div[2]/div[3]/div/select/option[4]").click()

    driver.find_element_by_xpath("//*[@id='type-wcard']").click()
    driver.find_element_by_xpath("//*[@id='checkbox_terms_traveler']").click()
    driver.find_element_by_xpath("//*[@id='reservation-btn']").click()




def ticket(driver):
    # 티켓 받는 곳까지 가는 기다림
    # 마이페이지 클릭
    WebDriverWait(driver, 1000000).until(EC.presence_of_element_located(
        (By.XPATH,
         "/html/body/div[3]/header/nav/div[1]/div[3]/ul/li[4]/a/img"))).click()

    driver.find_element_by_xpath(
         "/html/body/div[3]/header/nav/div[1]/div[3]/div/ul/li[2]/div[2]").click()
    time.sleep(1)

    #구매후 티켓 위치에 따른다
    WebDriverWait(driver, 10).until(EC.presence_of_element_located(
        (By.XPATH,
         "/html/body/main/div/div[4]/div[2]/div[2]/div/a"))).click()



def clk_ticket(driver):
    #티켓 버튼 클릭
    #driver.implicitly_wait(100000000)
    driver.set_script_timeout(10)
    WebDriverWait(driver, 10000).until(EC.presence_of_element_located(
        (By.XPATH,
         "//*[@id='vouchersBtn']"))).click()
    #driver.set_script_timeout(10)
    #티켓 출력

    for n in range(quantity + 1):
        tck_path = ["/html/body/main/div/div[4]/div[3]/div/div[1]/div[3]/div[1]/a",
                    "/html/body/main/div/div[4]/div[3]/div/div[1]/div[3]/div[2]/a",
                    "/html/body/main/div/div[4]/div[3]/div/div[1]/div[3]/div[3]/a",
                    "/html/body/main/div/div[4]/div[3]/div/div[1]/div[3]/div[4]/a"]
        driver.find_element_by_xpath(tck_path[n]).click()


    #구매한 시간 구하기
    buy_time = driver.find_element_by_xpath("/html/body/main/div/div[4]/div[4]/div/div[2]/div/div[1]/div[1]/div[2]")
    print(buy_time)


def download(url , file_name):
    with open(file_name, "wb")as file:
        response = get(url)
        file.write(response.content)
if __name__ == "__main__":
    #driver = webdriver.Chrome('\Users\owner\macro\chromedriver')
    quantity = input("how many tickets do you want to buy? :")

    product = input("what product do you want buy? \n"
                    "hkdiseny = 0  \n uss = 1 \n"
                    ":")
    prc_date = input("reservation date :")

    total_trans = int(quantity) / 4
    #quantity = 4 - 1
    number = input("what account do you want to buy : ")
    #USER = ac_var.myreal_users[number]
    #USER_DM = ac_var.myreal_user_domain[number]
    #USERID = USER + USER_DM
    #PASSWORD = "tongsung8116!"
    #rsv_date = 2

    # reserve user info
    #F_NAME = USER
    #L_NAME = USER[0]
    #FULL_NAME = F_NAME + "." + L_NAME
    #BIRTH_DATE = "881225"
    #PHONE_NB = "01072518121"


    #driver = webdriver.Firefox()
    driver = webdriver.Chrome('/Users/owner/PycharmProjects/MakePerson/mr/buyer/chromedriver')

   # driver.wait = WebDriverWait(driver, 2)
  #  driver.implicitly_wait(10)
    #driver.fullscreen_window()
    driver.get(myreal_HOMEPAGE)
    buy_time_list = []
    UserNumList = []
    UserList = []
    for i in range(int(total_trans)):
        quantity = 4 - 1
        USER = ac.MrKimnKimsUser[int(number) + i]
        USER_DM = "@kimnkims.com"
        USERID = USER + USER_DM
        PASSWORD = "tongsung8116!"
        rsv_date = prc_date

        #유저정보   user
        #구매일자   rsv_date
        #수량 리스트 qunt_list
        F_NAME = USER
        L_NAME = USER[0]
        FULL_NAME = F_NAME + "." + L_NAME
        BIRTH_DATE = "950507"
        PHONE_NB = "11111111111"

        login(driver)
        driver.get(myreal_ITEMURL[int(product)])
        checkOpt(driver)
        driver.set_script_timeout(10)
        checkOpt_qut(driver)
        # driver.wait
        # checkout(driver)
        driver.set_script_timeout(10)
        driver.implicitly_wait(10)
        driver.set_script_timeout(70)
        order(driver)
        ticket(driver)
        #clk_ticket(driver)

        #구매시간
        bytime = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH,
            "/html/body/main/div/div[4]/div[4]/div/div[2]/div/div[1]/div[1]/div[2]"
            ))).text
        buy_time_list.append(bytime)

        UserList.append(USER)
        UserNumList.append(int(number) + i)
        #다음 계정으로 넘어가기
        time.sleep(6)
        logout(driver)
        WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH,
                                       "/html/body/div[3]/header/nav/div[1]/div[3]/ul/li[3]/a"
                                       ))).click()
        driver.refresh()

    print(buy_time_list)
    # index_format(index) & columns_format(columns)정의
    # 열
    total_transList = []
    for i in range(int(total_trans)):
        total_transList.append(i)


    # 행
    columns_format = ['계정번호', '계정이름', '상품', '업체', '결제수단', '수량', '개당가격', '날짜', '결제시간']

    # DataFrame 초기화
    values = pd.DataFrame(index=total_transList, columns=columns_format)

    # x & y 값 정의

    for ii in range(values.shape[0]):
        values.iloc[ii, 0] = UserNumList[ii]  #계정번호
        values.iloc[ii, 1] = UserList[ii]  #계정이름
        values.iloc[ii, 2] = product   #상품
        values.iloc[ii, 3] = "mr"  #업체
        values.iloc[ii, 4] = "신한카드"  #결제수단
        values.iloc[ii, 5] = 4  #수량상품
        values.iloc[ii, 6] = 48,100  #개당가격
        values.iloc[ii, 7] = prc_date  #날짜
        values.iloc[ii, 8] = buy_time_list[ii]  #결제시간


    # saves DataFrame(values) into an Excel file
    values.to_excel('./test.xlsx',
                    sheet_name='Sheet1',
                    columns=columns_format,
                    header=True,
                    index=total_transList,
                    index_label="제목",
                    startrow=1,
                    startcol=0,
                    engine=None,
                    merge_cells=True,
                    encoding=None,
                    inf_rep='inf',
                    verbose=True,
                    freeze_panes=None)


