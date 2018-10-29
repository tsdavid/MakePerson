#-*- coding: utf-8 -*-
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.common.action_chains import ActionChains
from bs4 import BeautifulSoup
from requests import get
import pandas as pd
import numpy as np



def login(driver , USERID , PASSWORD):
    #아이디 넣는 곳
    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH,
       "//*[@id='userid']"
       ))).send_keys(USERID)
    #비밀번호 넣는 곳
    driver.find_element_by_xpath(
        "//*[@id='pwd']"
        ).send_keys(PASSWORD)
    #로그인 버튼
    driver.find_element_by_xpath(
         "//*[@id='loginFrm']/a[2]"
        ).click()


def logout(driver):
    driver.find_element_by_xpath("//*[@id='header2']/div/div[1]/div[1]/ul/li[2]/a").click()
def reservation(driver , quantity):
    #성인권 클릭
    driver.find_element_by_xpath(
        "//*[@id='li_1533302018_0']"
    ).click()

    #수량조절
    i = 0
    while i < int(int(quantity) - 1):
        driver.find_element_by_xpath(
        "//*[@id='content']/div[2]/div[2]/div[5]/ul/li/span[2]/span/a[1]"
                                 ).click()
        i += 1

    #구매버튼
    driver.find_element_by_xpath(
        "//*[@id='buy_button']"
    ).click()


def order(driver , Name , FIrName , Email , PayBank):
    #사용자정보 변경
    time.sleep(6)
    driver.find_element_by_xpath(
             "//*[@id='_buyer']/div/table/thead/tr/td/label[2]/em"
     ).click()
    driver.find_element_by_xpath(
        "//*[@id='_buyer_others_name']"
    ).send_keys(FIrName+Name) #풀네임
    driver.find_element_by_xpath("//*[@id='_buyer_others_phone1']").send_keys("7251") #전화번호 앞자리
    driver.find_element_by_xpath("//*[@id='_buyer_others_phone2']").send_keys("8121") #전화번호 뒷자리
    driver.find_element_by_xpath("//*[@id='_buyer_others_email']").send_keys(Email)


    #여권영문 이름
    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH,
        "//*[@id='_custom_fields']/div/div/table/tbody/tr[1]/td/input"
           ))).send_keys(Name)
    #여권영문 성
    driver.find_element_by_xpath(
        "//*[@id='_custom_fields']/div/div/table/tbody/tr[2]/td/input"
    ).send_keys(FIrName)
    # 이메일 주소
    driver.find_element_by_xpath(
        "//*[@id='_custom_fields']/div/div/table/tbody/tr[3]/td/input"
    ).send_keys(Email)

    #카드 종류 선택
    driver.find_element_by_xpath("//*[@id='_iselect_payInfo_card']").click()
    time.sleep(1)

   #결제 카드사 선택
    PayCard = "//*[@id='_iselect_payInfo_card']/option[" +  PayBank  + "]"
    driver.find_element_by_xpath(
        PayCard
    ).click()

    # 약관동의
    driver.find_element_by_xpath(
        "//*[@id='_terms']/dl/dt/label"
    ).click()

    # 결제하기 버튼
    driver.find_element_by_xpath(
        "//*[@id='_confirmCheckout']"
    ).click()

    time.sleep(0.5)

    #버튼 클릭 후 팝업 확인버튼 클릭
    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH,
       "//*[@id='_continueConfirm']"
       ))).click()


#결제부분
def Payment(driver):
    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH,
       "/html/body/div/ul/li[2]/a"
       ))).click()
def wait(driver):
    WebDriverWait(driver, 100000000000).until(EC.presence_of_element_located((By.XPATH,
       "//*[@id='_header']/div/h3"
       )))