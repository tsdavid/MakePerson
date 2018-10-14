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
import sys
from buyer import functions  as fc
from general import codes as cd



driver = webdriver.Chrome('/Users/owner/PycharmProjects/MakePerson/mr/chromedriver')
driver.get(cd.company_code[0]['finish_url'])
fc.login(driver , 'brown@poongsung.me' , 'tongsung8116!')
time.sleep(2)
driver.find_element_by_xpath("/html/body/main/div/div[4]/div[2]/div[2]/a[1]").click()
time.sleep(1)
driver.find_element_by_xpath("//*[@id='vouchersBtn']").click()
# 티켓 html 가지고오기
driver.implicitly_wait(10)
html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')
noti = soup.select('a.voucher-btn')


time.sleep(2)
# 바우처 리스트에 저장
voucher_list = []
for i in range(4):
    voucher = str(noti[i])[29:178]
    voucher_list.append(voucher)
print(voucher_list)

# clk_ticket(driver) 티켓 출력하는 함수
now = datetime.now()
for i in range(4):
    fc.download(voucher_list[i], "uss" + "mr" + str(now.minute) + str(now.second) + "_asaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaasssssssssssssss" + str(i) + ".pdf")
