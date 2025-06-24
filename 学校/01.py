# a=int(input('输入第一个数'))
# b=int(input('输入第二个数'))
# print("这俩数的和是",a+b)
from os.path import split

#改变print的输出结束符号
# a=int(input('输入第一个数'))
# b=int(input('输入第二个数'))
# print('a',end='')
# print('+',end='')
# print('b',end='')
# print('=',end='')
# print(a+b)

# 遍历列表的元素并相加
# list1=[1,2,3,4,5,6]
# print(len(list1))
# totals=0
# for total in  list1:
#     totals += total
# print(totals)

#查询字符的Unicode代码
# a=input('你想要查询的字符')
# print(ord(a))

#查询Unicode代码对应的代码
# a=int(input('你想要查询的代码'))
# print(chr(a))


# a = str(input())
# print(str.upper(a))

# a = float(input())
# b = a % 1
# b = round(b, 1)
# c = a % 10 - b
# d = (a % 100 - a % 10)/10
# e = a // 100
# f = b * 10 + c * 0.1 + d*0.01 + e*0.001
# f = round(f, 3)
# print(f)

# t ,n= input().split( )
# # t = float(t)
# # n = int(n)
# # a = float(t/n)
# # a = round(a,3)
# # print(a)
# # print(2*n)

# a ,b ,c =input().split( )
# a=int(a)
# b=int(b)
# c=int(c)
# p = (a + b + c)/ 2
# s = (p*(p-a)*(p-b)*(p-c)) ** (1/2)
# s = round(s, 1)
# print(s)

s,v = map(int,input().split())
