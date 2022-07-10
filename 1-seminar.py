#Задача 1: на вход 2 числа и проверка является ли одно квадратом другого
'''
 firstNum = int(input('enter first num:  '))
 secondNum = int(input('enter second num:  '))
 if firstNum < secondNum:
     x = firstNum
     y = secondNum
 else:
     x = secondNum
     y = firstNum

 def check(a,b):
     if b == a*a:
         return f'yes'
     else:
         return f'no'

 print (check(x,y))
'''
#Задача2: ввод 5 чисел, найти максимальное
'''
string_list = input("введите числа через пробел:  ").split()
num_list = list(map(int,string_list))
print (num_list)

def find_max(list):
    max = list[0]
    for i in list:
        if max<i:
            max=i
    return(max)

print (find_max(num_list))
'''
#Задача 3: на вход N, на выход от -N до N
'''
N = int(input("введите число N:  "))

def get_list(a):
    if a < 0: 
        a=a*-1
    numbers = list(range(-a, a+1))
    return (numbers)

print(get_list(N))
'''
#На вход дробь, показывать первую цифру дробной части числа.
N =input('введите дробное число:  ')
string = N.split('.') #31.478
try:
    string2 = string[1]
    print(string2[0])
except:
    print('число не дробное')


#На вход число и проверяет, кратно ли оно 5 и 10 или 15, но не 30.
