pdfFileObj = open(voucher_name, 'rb')  # 'rb' for read binary mode
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

pageObj = pdfReader.getPage(0)  # '9' is the page number
vou_reserCode = 'mr' + '_' + 'uss' + '_' + str(pageObj.extractText())[13:31] + '.pdf'
print(vou_reserCode)

pdfFileObj.close()

ff = '/Users/user/PycharmProjects/MakePerson/mr/downloader/' + voucher_name
ffr = ff.replace(voucher_name, vou_reserCode)
os.rename(ff, ffr)
time.sleep(5)
# 다음 계정으로 넘어가기
fc.logout(driver)
WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH,
                                                               "/html/body/div[3]/header/nav/div[1]/div[3]/ul/li[3]/a"
                                                               ))).click()
driver.refresh()