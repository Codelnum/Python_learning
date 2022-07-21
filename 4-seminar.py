#1. Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
#*Пример:*
#- [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12
'''
import random

list_length = int(input("input list_length:  "))
def get_list(n):
    list = []
    for i in range(n):
        list.append(random.randint(1,10))
    return list
gen_list = get_list(list_length)
print(gen_list)

def odd_sum(list):
    sum=0
    for (index, i) in enumerate(list):
        if index %2!=0:
            sum=sum+i
    return sum
sum = odd_sum(gen_list)
print(sum)


'''
#2. Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
#*Пример:*

# [2, 3, 4, 5, 6] => [12, 15, 16];
# [2, 3, 5, 6] => [12, 15]
'''
import random

list_length = int(input("input list_length:  "))
def get_list(n):
    list = []
    for i in range(n):
        list.append(random.randint(1,10))
    return list
gen_list = get_list(list_length)
print(gen_list)

def get_multi_list(list):
    result_list = []
    for i in range(0,len(list)):
        result_list.append(list[i]*list[-i-1])
        if i >= len(list)/2-1:
            break
    return result_list
mult_list = get_multi_list(gen_list)
print(mult_list)
'''
#3. Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
#*Пример:*
#- [1.1, 1.2, 3.1, 5, 10.01] => 0.19
'''
start_list = [1, 1.2, 3.1, 5, 10.01]

def get_x_list(list):
    x_list = []
    for i in list:
        if i%1==0:
            i+1
        else:
            x_list.append(round(i%1,3))
    return x_list
x_list = get_x_list(start_list)
print(x_list)

def find_ext(list):
    max = list[0]
    min = list[0]
    for i in list:
        if i>= max: max =i
        if i <= min: min = i
    ext=round(max-min, 3)
    return ext, min, max

print(find_ext(x_list))




'''
#4. Напишите программу, которая будет преобразовывать десятичное число в двоичное.
#*Пример:*
# 45 -> 101101
# 3 -> 11
# 2 -> 10
'''
num = int(input("input num: ")) 

def get_bin(n):
    list = []
    while n>0:
        list.append(n%2)
        n=n//2
    return list

rev_list = get_bin(num)[::-1]
bin = int(''.join(map(str, rev_list)))

print(bin)



'''
#5. Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

#*Пример:*

#- для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 

num = int(input("input num: "))
f1=0
f2=1

def sum(a,b):
    n= a+b
    return n
def neg_sum(a,b):
    n=(a-b)
    return n

def get_list1(a,b, num):    
    list1=[]
    for i in range(0,num):
        n=sum(a,b)       
        list1.append(n)
        a = b
        b = n
    return list1              
def get_list2(a,b, num):
    list2=[] 
    for i in range(0,num):      
        n=neg_sum(a,b)       
        list2.append(n)
        a = b
        b = n
    return list2 

list1 = get_list1(f1,f2,num)
list2 = get_list2(f1,f2,num)
list2.reverse()
fibo_list = [f1,f2]
fibo_list.extend(list1)
print(list2+fibo_list)