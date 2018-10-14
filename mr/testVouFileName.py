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


voucher = "https://s3.amazonaws.com/myrealtrip-bulk-invoice-tracked-production/21988/133569/8dc0d20e93f9b2ebb9b3bf478a73714bb49dbded1ce1440b19e2e004eba5b13b.pdf"
fc.download(voucher, "uss" + "mr" +"_asaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaasssssssssssssss" + ".html")