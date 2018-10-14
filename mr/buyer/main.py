#-*- coding: utf-8 -*-
import sys
import random
import functions as fc
from myreal import mr_vars as mrvr
from waug import wgfunction as wgfc
import codes as cd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.common.action_chains import ActionChains

#구매전 정보 받는 함수
def question():
    global quantity
    global company
    global product
    global prc_date
    global select_account
    quantity = input("how many tickets do you want to buy? :")
    company = input("which company do you want buy from?  \n"
                    "myreal = 0 \n"
                    "waug = 1\n"
                    "enter ::::: ")
    product = input("what product do you want buy? \n"
                    "hkdiseny = 91  \n uss = 90 \n"
                    ":")
    prc_date = input("reservation date :")
    select_account = input("which accounts do you want to start?")

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


if __name__ == "__main__":
    question()
    #driver = webdriver.Firefox()
    driver = webdriver.Chrome('/Users/user/PycharmProjects/buyer/chromedriver')



    driver.get(cd.company_code[company]['login_url'])



    cal(quantity, cd.company_code[company]['buy_rule'])


    quantity_list = []
    for i in range(int(perfect_trans)):
        quantity_list.append(nomal_rule)
    quantity_list.append(float(remainder) * int(nomal_rule))

    buyurl_code = 'item_url_' + str(product)



    #일단 perfect_trans로 for를 준다 total_trans로 주게되면 나머지값에 대한 구매 처리가 생각하기 어려움
    for i in range(int(perfect_trans)):
        fc.login(driver , mrvr.myreal_users[int(select_account) + i] + mrvr.myreal_user_domain[int(select_account) + i] , "tongsung8116!")
        driver.get(print(cd.company_code[company][buyurl_code]))
        fc.reservation(driver , prc_date , quantity)
        fc.res_date(driver , int(prc_date))
        fc.res_qunt(driver , int(quantity_list[i]))
        fc.order(driver , mrvr.myreal_users[int(select_account) + i][0] , mrvr.myreal_users[int(select_account) + i] ,mrvr.myreal_users[int(select_account) + i] + "." + mrvr.myreal_users[int(select_account) + i][0] , random.choice(mrvr.birth_date_list), "01072518121")
        fc.ticket(driver)
        fc.clk_ticket(driver , int(quantity_list[i]))
        fc.logout(driver)
