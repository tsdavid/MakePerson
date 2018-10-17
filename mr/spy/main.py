#HeadLess Chrome으로 창 없이 크롤링 만들기
import sys
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.common.action_chains import ActionChains
from bs4 import BeautifulSoup
from general import CoorpAgent as ca




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



options = webdriver.ChromeOptions()
options.add_argument('headless')
options.add_argument('window-size=1920x1080')
options.add_argument('--disable-gpu')

#유의: chromedriver를 위에서 받아준
#chromedriver(windows는 chromedriver.exe)의 절대경로로 바꿔주세요.!
#driver = webdriver.Chrome('/Users/user/PycharmProjects/buyer/chromedriver')
driver = webdriver.Chrome('/Users/owner/PycharmProjects/MakePerson/mr/spy/chromedriver',options=options)

driver.get('https://www.myrealtrip.com/offers/15441')
driver.implicitly_wait(3)
reservation(driver , 20 , 1)
price = driver.find_element_by_xpath(
    "//*[@id='SearchFormContainer-react-component-2b11c5e4-b13c-431a-9199-6e6e7b544eac']/div/div[2]/form/div[1]/div[2]/div[2]/div[2]/div/div[3]"
).text
print(price)



driver.quit()