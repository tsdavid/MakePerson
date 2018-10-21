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
    print("logout function")

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


def order(driver , Name , FIrName , Email):
    #여권영문 이름
    driver.find_element_by_xpath(
        "//*[@id='_custom_fields']/div/div/table/tbody/tr[1]/td/input"
    ).send_keys(Name)
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

    """  카드 정보ㅉ는 
    //*[@id="_iselect_payInfo_card"]/option[8]
    이  포맷에서 맨 뒤 숫자 8만 바뀌는 듯
    2 : 신한
    3 : 국민
    4 : BC
    5 : 현대
    6 : 우리
    7 : 하나
    8 : KEB
    9 : NH
     11: 롯데
    
    
    """