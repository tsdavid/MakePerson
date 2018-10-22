# -*- coding: utf-8 -*-
import random
import sys

sys.path.insert(0, '/Users/user/PycharmProjects/MakePerson/mr/general/')
import functions  as fc
import accounts as ac
import codes as cd

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.common.action_chains import ActionChains
import pandas as pd
import numpy as np

if __name__ == "__main__":
    # 미리 받는 정보
    ResultQuest = fc.question()
    ResultCal = fc.cal(ResultQuest[0], cd.company_code['buy_rule'])
    # fc.question[o] #총 수량 TotalAmount
    # fc.question[1] #상품 코드 product
    # fc.question[2] #예약할 날짜 prc_date
    # fc.question[3] #계정 번호 select_account

    # 드라이버 선택
    # driver = webdriver.Firefox()
    driver = webdriver.Chrome('/Users/user/PycharmProjects/MakePerson/mr/buyer/chromedriver')

    # total_trans , real_trans , perfect_trans , remainder
    # fc.cal(101,4)[0]  #total_trans
    # fc.cal(101,4)[1]  #real_trans
    # fc.cal(101,4)[2]  #perfect_trans
    # fc.cal(101,4)[3]  #remainder

    # quantity_list 는 구매횟수 저장한 리스트
    quantity_list = []
    for i in range(int(ResultCal[2])):
        quantity_list.append(cd.company_code['buy_rule'])
    quantity_list.append(float(ResultCal[3]) * int(cd.company_code['buy_rule']))

    buyurl_code = 'item_url_' + str(ResultQuest[1])

    UserList = []
    BuyTimeList = []
    # 일단 perfect_trans로 for를 준다 total_trans로 주게되면 나머지값에 대한 구매 처리가 생각하기 어려움

    for i in range(len(quantity_list)):
        # 로그인 URL
        driver.get(cd.company_code['login_url'])
        fc.login(driver, ac.MrKimnKimsUser[int(ResultQuest[3]) + i] + "@kimnkims.com", "tongsung8116!")
        driver.get(cd.company_code[buyurl_code])
        fc.reservation(driver, ResultQuest[2], quantity_list[i])
        fc.order(driver, ac.MrKimnKimsUser[int(ResultQuest[3]) + i][0], ac.MrKimnKimsUser[int(ResultQuest[3]) + i],
                 ac.MrKimnKimsUser[int(ResultQuest[3]) + i] + "." + ac.MrKimnKimsUser[int(ResultQuest[3]) + i][0],
                 950901, "11111111111")
        fc.ticket(driver)
        # fc.clk_ticket(driver , int(quantity_list[i]))

        BuyTime = driver.find_element_by_xpath(
            "/html/body/main/div/div[4]/div[4]/div/div[2]/div/div[1]/div[1]/div[2]"

        ).text

        UserList.append(ac.MrKimnKimsUser[int(ResultQuest[3]) + i])
        BuyTimeList.append(BuyTime)

        fc.logout(driver)

    fc.PrintExcel2(quantity_list, UserList, ResultCal[2], BuyTimeList)

    # 구매횟수를 quantitly_list으로 했으니까 이제 티켓을 클릭하는 것도 그렇게 하면됨