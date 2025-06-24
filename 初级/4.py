# com = '拳头'
# player = int(input('你出什么?输入序号  1.剪刀 2.石头 3.布'))
# if player == 1:
#     print('电脑出的拳头,你输了')
# elif player == 2:
#     print('平局')
# elif player == 3:
#     print('你赢了,电脑出的拳头')
# else:
#     print('没按要求来,直接判你输!!!')
#





# num = 1
# user_name ='hyp'
# ps = 'hyp123456'
# while True:
#     name = input('请输入你的用户名:')
#     if name == user_name:
#         password = input('请输入输入你的密码')
#
#         if password == ps:
#             print('登陆成功')
#             break
#         else:
#             print('请重新输入密码')
#             num += 1
#             if num > 3:
#                 print('您已输错三次密码,登录失败,锁定账户')
#                 break
#             else:
#                 continue
#
#     else:
#         break



# boy = int(input('请输入男生的年龄:'))
# girl = int(input('请输入女生的年龄:'))
# if boy >= 22 and girl >= 20:
#     print('你俩可以结婚了')
# else:
#     print('你俩没到岁数,没法结婚')


num = 1
list01 = [1 ,3 ,5 ,4,3, 3 ,2]
for i in list01:
    num =num*i
print(num)