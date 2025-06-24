# num =1
# for i in range(100,1000):
#     if i //100 == i%10:
#         print(i)
#         num += 1
#     else:
#         continue
# print(f'有{num}个大于100小于1000的对偶数')


while True:
    num = eval(input('请输入一个整数:'))
    if num == -1:
        break
    elif type(num) ==type(1) :
        continue
    else:
        print('输入错误请重新输入')
