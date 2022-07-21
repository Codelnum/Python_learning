#Вычислить результат деления двух чисел c заданной точностью d
'''
from decimal import Decimal, getcontext

num1 = Decimal(input("input num1:  "))
num2 = Decimal(input("input num2:  "))
getcontext().prec = int(input("input precision(1-10):  "))
print(num2/num1)
'''
#Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
num = int(input("input num:  "))

def find_factor(n):
    value_list = []
    d = 2
    while d * d <= n: #5
        if n % d == 0:
            value_list.append(d)
            n //= d
        else:
            d += 1
    if n > 1:
        value_list.append(n)
    if len(value_list)<2:
        return "простое число"
    else:
        return value_list

print(find_factor(num))