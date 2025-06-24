# num = int(input('输入一个数:'))
# a = 1
# for i in range(32):
#     a *= num
#     print(a)

# txt = str(input('输入一段文字'))
# for i in txt:
#     print(i)

# num = input('请输入一个算式:')
# num1 = eval(num)
# print(num1)

# grade = eval(input('输入成绩'))
# if not isinstance(grade, (int, float)):
#     print("输入不合法，请输入数字")
# if grade < 0 or grade > 100:
#     print("输入不合法，请输入0到100之间的数字")
# if grade < 60:
#     print("不及格")
# if grade < 80 and grade >= 60:
#     print ("及格")
# if grade < 90 and grade >= 80:
#     print ("良好")
# if grade < 100 and grade >= 90:
#     print("优秀")

#
# grade = eval(input('输入成绩'))
# if not isinstance(grade, (int, float)):
#     print("输入不合法，请输入数字")
# elif grade < 0 or grade > 100:
#     print("输入不合法，请输入0到100之间的数字")
# elif grade >= 90:
#     print('优秀')
# elif grade >= 80:
#     print('良好')
# elif grade >= 60:
#     print('及格')
# else:
#     print('不及格')
#
# def find_narcissistic_numbers_method1():
#     for num in range(100, 1000):
#         hundreds = num // 100
#         tens = (num // 10) % 10
#         ones = num % 10
#         if num == hundreds ** 3 + tens ** 3 + ones ** 3:
#             print(num)
#
#
# find_narcissistic_numbers_method1()


# def find_narcissistic_numbers_method2():
#     for num_str in map(str, range(100, 1000)):
#         digits = [int(digit) for digit in num_str]
#         cube_sum = sum(digit ** 3 for digit in digits)
#         if int(num_str) == cube_sum:
#             print(int(num_str))
#
#
# find_narcissistic_numbers_method2()



# 初始化一个字典来存储每个数的因子和
divisor_sums = {}
# 初始化一个集合来存储已经找到的亲密数对
amicable_pairs = set()

# # 遍历2000以内的所有整数m，并计算它们的因子和
# for m in range(2, 2000):
#     sum_of_divisors = 1
#     for i in range(2, int(m**0.5) + 1):
#         if m % i == 0:
#             sum_of_divisors += i
#             if i != m // i:
#                 sum_of_divisors += m // i
#     divisor_sums[m] = sum_of_divisors  # 存储因子和
#
# # 检查亲密数对
# for m in divisor_sums:
#     n = divisor_sums[m]
#     if m != n and divisor_sums.get(n, 0) == m:  # 检查n的因子和是否等于m
#         # 由于亲密数对(m, n)和(n, m)是等价的，我们只存储升序对
#         amicable_pairs.add((min(m, n), max(m, n)))
#
# for pair in sorted(amicable_pairs):
#     print(pair)


import turtle
import random
screen = turtle.Screen()
screen.bgcolor("white")
pen = turtle.Turtle()
pen.speed(0)
num_rings = 6
radius_step = 30
base_radius = radius_step * (num_rings + 1)
def random_color():
    return f"#{random.randint(0, 0xFFFFFF):06x}"
for i in range(num_rings):
    outer_radius = base_radius - i * radius_step - radius_step // 2
    inner_radius = outer_radius - radius_step
    pen.penup()
    pen.setpos(0, -outer_radius)  # 圆心在(0, -radius)处
    pen.pendown()
    ring_color = random_color()
    pen.color(ring_color)
    pen.begin_fill()
    pen.circle(inner_radius)  # 绘制内圆并填充
    pen.end_fill()
pen.hideturtle()
turtle.done()
turtle.done()