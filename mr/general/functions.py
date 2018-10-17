#-*- coding: utf-8 -*-
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.common.action_chains import ActionChains
from bs4 import BeautifulSoup
from requests import get


#functions


#log in
def login(driver , USERID , PASSWORD):
    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH,
       "//*/input[@name='user[email]']"
       ))).send_keys(USERID)
    driver.find_element_by_xpath(
        "//*/input[@name='user[password]']"
        ).send_keys(PASSWORD)
    login_but = driver.find_element_by_xpath(
         "/html/body/main/div/div/div[3]/form/div/div[4]/button"
        )
    login_but.click()


def logout(driver):
    #click the uppon img
    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH,
        "/html/body/div[3]/header/nav/div[1]/div[3]/ul/li[4]/a/img"
        ))).click()
    #click the log out btn
    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH,
       "/html/body/div[3]/header/nav/div[1]/div[3]/div/ul/li[5]/div"
       ))).click()

#def res_date 와 res_res.qunt 종합
def reservation(driver , prc_date ,quantity ):

    #예약 날짜
    WebDriverWait(driver, 100).until(EC.presence_of_element_located((By.XPATH,
                             "//*[@id='calendarBtn']"
                             ))).click()
    # driver.find_element_by_xpath("//*[@id='calendarBtn']").click()
    # 상품날짜 선택

    WebDriverWait(driver, 100).until(EC.presence_of_element_located((By.LINK_TEXT,
                             str(prc_date)
                             ))).click()


    #수량 조절 시작
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
    while i < quantity:
        element.click()
        i += 1

    WebDriverWait(driver, 100).until(EC.presence_of_element_located((By.XPATH,
                                     "//*[@id='checkPriceBtn']/button"
                                     ))).click()

    time.sleep(1)
    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH,
                       "/html/body/main/section/div[2]/div[1]/div[2]/div[3]/div/div[2]/form/div[2]/div/div[2]/button"
                       ))).click()


#name change "checkOpt" -> "res_date"
def res_date(driver , prc_date):
    #상품날짜 설정 버튼 클릭
    WebDriverWait(driver, 100).until(EC.presence_of_element_located((By.XPATH,
         "//*[@id='calendarBtn']"
         ))).click()
    #driver.find_element_by_xpath("//*[@id='calendarBtn']").click()
    #상품날짜 선택

    WebDriverWait(driver, 100).until(EC.presence_of_element_located((By.LINK_TEXT,
         str(prc_date)
         ))).click()


#name change "checkOpt_qut" -> "res_qunt"
def res_qunt(driver , quantity):
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
    while i < quantity:
        element.click()
        i += 1

    WebDriverWait(driver, 100).until(EC.presence_of_element_located((By.XPATH,
                                     "//*[@id='checkPriceBtn']/button"
                                     ))).click()

    time.sleep(1)
    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH,
                       "/html/body/main/section/div[2]/div[1]/div[2]/div[3]/div/div[2]/form/div[2]/div/div[2]/button"
                       ))).click()

def order(driver , L_NAME , F_NAME ,FULL_NAME , BIRTH_DATE , PHONE_NB):
    WebDriverWait(driver, 100).until(EC.presence_of_element_located((By.XPATH,
         "/html/body/main/section/div/form/div[2]/div[1]/div[2]/div/div[2]/div[2]/input"
             ))).send_keys(L_NAME)
    driver.find_element_by_xpath(
        "/html/body/main/section/div/form/div[2]/div[1]/div[2]/div/div[3]/div[2]/input"
        ).send_keys(F_NAME)
    driver.find_element_by_xpath(
        "/html/body/main/section/div/form/div[2]/div[1]/div[2]/div/div[4]/div[2]/input"
         ).send_keys(FULL_NAME)
    driver.find_element_by_xpath(
        "//*[@id='input-icc']"
          ).click()
    driver.find_element_by_xpath(
        "/html/body/main/section/div/form/div[2]/div[1]/div[2]/div/div[5]/div[2]/select/option[2]"
        ).click()
    driver.find_element_by_xpath(
        "/html/body/main/section/div/form/div[2]/div[1]/div[2]/div/div[6]/div[2]/input"
        ).send_keys(BIRTH_DATE)
    driver.find_element_by_xpath(
        "/html/body/main/section/div/form/div[2]/div[2]/div[2]/div/div[1]/div[2]/div[2]/input"
        ).send_keys(PHONE_NB)
    driver.find_element_by_xpath(
        "/html/body/main/section/div/form/div[2]/div[2]/div[2]/div/div[2]/div[2]/div/select"
        ).click()
    driver.find_element_by_xpath(
        "/html/body/main/section/div/form/div[2]/div[2]/div[2]/div/div[2]/div[2]/div/select/option[5]"
        ).click()
    driver.find_element_by_xpath(
        "/html/body/main/section/div/form/div[2]/div[2]/div[2]/div/div[2]/div[3]/div/select"
        ).click()
    driver.find_element_by_xpath(
        "/html/body/main/section/div/form/div[2]/div[2]/div[2]/div/div[2]/div[3]/div/select/option[4]"
        ).click()

    driver.find_element_by_xpath(
        "//*[@id='type-wcard']"
        ).click()
    driver.find_element_by_xpath(
        "//*[@id='checkbox_terms_traveler']"
        ).click()
    driver.find_element_by_xpath(
        "//*[@id='reservation-btn']"
        ).click()


def ticket(driver):
    # 티켓 받는 곳까지 가는 기다림
    # 마이페이지 클릭
    WebDriverWait(driver, 1000000).until(EC.presence_of_element_located((By.XPATH,
         "/html/body/div[3]/header/nav/div[1]/div[3]/ul/li[4]/a/img"
         ))).click()
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,
         "/html/body/div[3]/header/nav/div[1]/div[3]/div/ul/li[2]/div[2]"
        ))).click()
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,
         "/html/body/main/div/div[4]/div[2]/div[2]/div/a"
        ))).click()



def clk_ticket(driver , quantity):
    #티켓 버튼 클릭
    #driver.implicitly_wait(100000000)
    driver.set_script_timeout(10)
    WebDriverWait(driver, 10000).until(EC.presence_of_element_located((By.XPATH,
         "//*[@id='vouchersBtn']"
               ))).click()


    for n in range(quantity + 1):
        tck_path = ["/html/body/main/div/div[4]/div[3]/div/div[1]/div[3]/div[1]/a",
                    "/html/body/main/div/div[4]/div[3]/div/div[1]/div[3]/div[2]/a",
                    "/html/body/main/div/div[4]/div[3]/div/div[1]/div[3]/div[3]/a",
                    "/html/body/main/div/div[4]/div[3]/div/div[1]/div[3]/div[4]/a"]
        driver.find_element_by_xpath(tck_path[n]).click()



    #구매한 시간 구하기
    buy_time = driver.find_element_by_xpath(
        "/html/body/main/div/div[4]/div[4]/div/div[2]/div/div[1]/div[1]/div[2]")
    #print(buy_time)

def cal(amount , rule):
    total_amount = float(amount)
    global nomal_rule
    nomal_rule = float(rule)
    global real_trans
    real_trans =  float(total_amount / nomal_rule) #25.25
    global total_trans
    total_trans = int(round(real_trans + 0.5)) #26
    global perfect_trans
    perfect_trans = round(real_trans - 0.5) #25
    global remainder
    remainder = real_trans - perfect_trans #0.25

    return real_trans , perfect_trans , remainder

def download(url , file_name):
    with open(file_name, "wb")as file:
        response = get(url)
        file.write(response.content)

