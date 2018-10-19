import sys
sys.path.insert(0, '/Users/owner/PycharmProjects/MakePerson/mr/general/')
import functions  as fc
import accounts as ac
import codes as cd

#fc.question[o] #총 수량 TotalAmount
#fc.question[1] #상품 코드 product
#fc.question[2] #예약할 날짜 prc_date
#fc.question[3] #계정 번호 select_account

ResultQuest = fc.question()
print(
    "TotalAmount : " + ResultQuest[0],
"product : " +  ResultQuest[1],
    "prc_date : " +ResultQuest[2],
    "select_account : " + ResultQuest[3]

)