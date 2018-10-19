import sys
sys.path.insert(0, '/Users/owner/PycharmProjects/MakePerson/mr/general/')
import functions  as fc
import accounts as ac
import codes as cd





#Function of Def Cal 's return value
# total_trans , real_trans , perfect_trans , remainder
# fc.cal(101,4)[0]  #total_trans
# fc.cal(101,4)[1]  #real_trans
# fc.cal(101,4)[2]  #perfect_trans
# fc.cal(101,4)[3]  #remainder

Amount = 101
BuyRule = 4
ResultCal = fc.cal(Amount,BuyRule)
print(fc.cal(101, 4)[0])


quantity_list = []
#일단 for로 Buyrule 만큼 늘릴꺼니까 range는 total_trans가 아니라 perfect_trans로 해야함
for i in range(int(ResultCal[2])):
    quantity_list.append(BuyRule)
#그리고 마지막에 remainder을 넣어준다
quantity_list.append(float(ResultCal[3]) * int(BuyRule))

print(quantity_list)
print(len(quantity_list))