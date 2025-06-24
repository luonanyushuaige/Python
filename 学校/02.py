money = int(input('请输入你的工资'))
money_1 = int(input('输入专项扣除金额'))
money_2 = int(input('输入你的专项附加扣除金额'))
num = money - money_1 - money_2 - 5000
if num >= 85000:
    num_1 = num *0.45 - 15160
elif num >= 55001:
    num_1 = num *0.35 - 7160
elif num >= 35001 :
    num_1 = num *0.3 - 4410
elif num >= 25001 :
    num_1 = num *0.25 - 2660
elif num >= 12001 :
    num_1 = num *0.20 - 1410
elif num >= 3001 :
    num_1 = num *0.10 - 210
elif num >= 0 and num <3000  :
    num_1 = num *0.03
else:
    print('请输入有效收入')
print('应交所得税额:',end='')
print(num)
print('个税:',end='')
print(num_1)