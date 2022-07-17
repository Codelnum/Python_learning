#Задача 1:
'''
num = int(input("input N:  "))

def get_sum(a):
    list=[]
    sum=0
    n=1
    for x in range(1,a+1):
        x = ((1+1/n)**n)
        list.append((f"{n}: {x}"))
        n+=1
        sum=sum+x
    return list, (f"Сумма чисел: {sum}")

print(get_sum(num)[0])
print(get_sum(num)[1])
'''
# Задача 2: сделать функцию, на вход принимающую список, на выходе возращающая словарь, где указаны:
#  максимальное число,
#  минимальное,
#  их индексы,
#  и среднее арифметическое 

input_list  = list(map(int, input("введите числа через пробел:  ").split() ))
length = len(input_list)


def find_min(list):
    min = list[0]
    for i in list:
        if i<min:
            min = i
            n = list.index(min)
    return min, n

def find_max(list):
    max = list[0]
    for i in list:
        if i>max:
            max = i
            n = list.index(max)
    return max, n

def get_average(list, n):
    sum=0
    i=0
    for i in list:
        sum=sum+i
    average = round(sum/n, 2)    #округление до 2 знака
    return average

dict = {'min':find_min(input_list)[0], 'index_min':find_min(input_list)[1], 'max':find_max(input_list)[0], 'index_max':find_max(input_list)[1], 'average_list':get_average(input_list, length) }
print(dict)

file = open('FirstDic.txt', 'w')
for a,b in dict.items():
    file.write(f'{a}: {b},  \n')
file.close()