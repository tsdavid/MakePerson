#-*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.alert import Alert
import requests

#로그인 함수
def login(driver , USERID , PASSWORD):
    time.sleep(1)
    #push the "login button" at main page
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,
        "//*[@id='navbar']/div/a[1]"
        ))).click()
    #send ID information at ID space
    time.sleep(1)
    driver.find_element_by_xpath("//*[@id='mem_id']").send_keys(USERID)
    driver.find_element_by_xpath("//*[@id='mem_pwd']").send_keys(PASSWORD)
    #click the login button
    driver.find_element_by_xpath("//*[@id='frm-login']/button").click()

    #now we can next stage, product page





#쿠폰 체크 함수 #mr functions에는 없는 함수
def coupon_check(driver):
    coupon_btn = driver.find_element_by_xpath("//*[@id='download-coupon']/div/div[2]")
    if coupon_btn is None:
        print ("No Coupon")
    else:
        coupon_btn.click()
        Alert(driver).accept()
        print ("Coupon is saved")


#바로 사용 가능하지 체크 함수 #mr fuctions 에서는 없는 함수
def checkStock(driver , outof_stock_URL):
    stock_check = driver.find_element_by_css_selector(".goodtitle-direct-imgsize img")
    if stock_check is None:
        print ("there is out of stock")
        driver.get(outof_stock_URL)
    else:
        #True
        print ("wow good job")
        coupon_check(driver)


#수량 및 예약 날짜 설정 함수

def reservation(driver ,quantity):
    
    #쿠폰 발급
    coupon_btn = driver.find_element_by_xpath("//*[@id='download-coupon']/div/div[2]")
    if coupon_btn is None:
        print("No Coupon")
    else:
        coupon_btn.click()
        time.sleep(2)
        Alert(driver).accept()
        print("Coupon is saved")


    driver.find_element_by_xpath(
        "//*[@id='s_date']"
    ).click()
    time.sleep(1)

    #WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR,
     #                                                                    "body > div.datepicker.datepicker-dropdown.dropdown-menu.datepicker-orient-left.datepicker-orient-bottom > div.datepicker-days > table > tbody > tr:nth-child(4) > td:nth-child(4)"
      #                                                                   ))).click()
    #오늘 날짜로 달력설정
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR,
        "td.today"
        ))).click()

    time.sleep(2)
    #상품 설정
    WebDriverWait(driver, 10000).until(EC.presence_of_element_located((By.XPATH,   #옵션을 선택해 주세요.
        "//*[@id='option-item-title']/div/span/span[1]/span"
        ))).click()
    time.sleep(1)
    WebDriverWait(driver, 10000).until(EC.presence_of_element_located((By.XPATH,  # USS 입장권
           "//*[@id='select2-parent_option-results']/li[2]"
    ))).click()


   #여기 하다가 안되서 있음
    #수량설정 1클릭
    i = 0
    while i < quantity:
        driver.find_element_by_xpath(
            "//*[@id='price_option_0-0']/div/div[2]/button[2]"
        ).click()
        i += 1


    #예약하기 버튼 클릭
    driver.find_element_by_xpath(
        "//*[@id='btn-order']"
    ).click()



#구매시 예약 정보 넣는 함수
def order(driver , F_NAME , MD_PHONE , LT_PHONE , L_NAME):
    WebDriverWait(driver, 10000000000).until(EC.presence_of_element_located((By.XPATH,
                        "//*[@id='frm-order-info']/div/div[2]/div[1]/input"
                            ))).send_keys(F_NAME)
    driver.find_element_by_xpath(
        "//*[@id='frm-order-info']/div/div[2]/div[2]/span[3]/input[1]"
        ).send_keys(MD_PHONE)
    driver.find_element_by_xpath(
        "//*[@id='frm-order-info']/div/div[2]/div[2]/span[3]/input[2]"
       ).send_keys(LT_PHONE)
    driver.find_element_by_xpath(
        "//*[@id='frm-order-info']/div/div[2]/div[3]/input[1]"
    ).send_keys(F_NAME)
    driver.find_element_by_xpath(
        "//*[@id='frm-order-info']/div/div[2]/div[3]/input[2]"
    ).send_keys(L_NAME)

    #입력완료 버튼 클릭
    driver.find_element_by_xpath(
        "//*[@id='btn-info-write']"
    ).click()


#결제 정보 넣는 함수
def payment(driver):
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,   #신용카드 선택
        "//*[@id='content']/form/div/div[2]/div/div[2]/div[1]/div/div/div/div/div[3]/div/label/p"
            ))).click()
    driver.find_element_by_xpath( #개인정보 제 3자 제공동의
        "//*[@id='chk-order-agree']"
    ).click()

    driver.find_element_by_xpath( #쿠폰함 클릭
        "//*[@id='btn-modal-coupon']"
    ).click()

    time.sleep(2)
    CoupCode = driver.find_element_by_xpath(
        "//*[@id='coupon-available']/div/div/div/div/div[1]/div/div/div[1]/div[2]/span"
    ).text
    if CoupCode == "USS7000":  #만약에 쿠폰 코드가 맞다면 쿠폰 사용하기 클릭
        driver.find_element_by_xpath(
            "//*[@id='coupon-available']/div/div/div/div/div[1]/div"
        ).click()
    driver.find_element_by_xpath(  #쿠폰 적용하기
        "//*[@id='btn-apply-coupon']"
         ).click()
    time.sleep(2)
    Alert(driver).accept()
    print("Coupon is applied")

    #포인트 사용
    time.sleep(3)
    driver.find_element_by_xpath(
        "//*[@id='order-point-form']/div[2]/button"
    ).click()


   #구매버튼
    WebDriverWait(driver, 2)
    driver.find_element_by_xpath("//*[@id='btn-order-pay']").click()
    #chk_coupon = driver.find_element_by_partial_link_text('USS')
    #chk_coupon = WebDriverWait(driver, 10).until(
    #    EC.presence_of_element_located((By.XPATH,"//div[@data-idx = '143056']//span"))).text()
    #chk_coupon = driver.find_element_by_xpath("//div[@data-idx = '143056']//span").text()
    #if chk_coupon == "USS7000":
    #    print "fuck no uss700 coupon"
 #   else:
   #     get_coupon.click()
    #    driver.find_element_by_xpath("//*[@id='btn-apply-coupon']").click()


#티켓을 킄릭하는 함수

def ticket(driver):
    WebDriverWait(driver, 10000).until(EC.presence_of_element_located((By.XPATH,
            "/html/body/div[1]/div[4]/div/div[2]/div[3]/div[2]/a"
           ))).click()
    WebDriverWait(driver, 100).until(EC.presence_of_element_located((By.XPATH,
            "/html/body/div[1]/div[4]/div/div/div/div[3]/div[1]/div[1]/div[2]"
             ))).click()

    #티켓클릭
    #WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,
     #   "/html/body/div[1]/div[4]/div[1]/div/div/div[3]/div/div[11]/div[1]/a/div"
      #  ))).click()

def etickt_clikc(driver):
    #나머지 클릭 나머지 9개
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH,
                                        "/html/body/div[1]/div[4]/div[1]/div/div/div[3]/div/div[11]/div[2]/a/div"))).click()
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH,
                                        "/html/body/div[1]/div[4]/div[1]/div/div/div[3]/div/div[11]/div[3]/a/div"))).click()
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH,
                                        "/html/body/div[1]/div[4]/div[1]/div/div/div[3]/div/div[11]/div[4]/a/div"))).click()
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH,
                                        "/html/body/div[1]/div[4]/div[1]/div/div/div[3]/div/div[11]/div[5]/a/div"))).click()
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH,
                                        "/html/body/div[1]/div[4]/div[1]/div/div/div[3]/div/div[11]/div[6]/a/div"))).click()
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH,
                                        "/html/body/div[1]/div[4]/div[1]/div/div/div[3]/div/div[11]/div[7]/a/div"))).click()
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH,
                                        "/html/body/div[1]/div[4]/div[1]/div/div/div[3]/div/div[11]/div[8]/a/div"))).click()
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH,
                                        "/html/body/div[1]/div[4]/div[1]/div/div/div[3]/div/div[11]/div[9]/a/div"))).click()
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH,
                                        "/html/body/div[1]/div[4]/div[1]/div/div/div[3]/div/div[11]/div[10]/a/div"))).click()


def logout(driver):
    WebDriverWait(driver, 1000000).until(EC.presence_of_element_located((By.XPATH,
        "//*[@id='navbar']/div/a[1]"
         ))).click()
def download(url , file_name):
    with open(file_name, "wb")as file:
        response = get(url)
        file.write(response.content)
