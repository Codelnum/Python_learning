#Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат. not(X or Y or Z) = not X and not Y and not Z
'''
x = input("input X: ")
y = input("input Y: ")
z = input("input Z: ")
list = [x,y,z]

def check(list):
    left = (not(list[0] or list[1] or list[2]))
    right =((not list[0]) and (not list[1]) and (not list[2]))
    result = left == right
    return result

print(check(list))
'''

# Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.
'''
point1 = list(map(int, input("введите координаты первой точки через пробел: ").split( )))
point2 = list(map(int, input("введите координаты  второй точки через пробел: ").split( )))
#from math import hypot
#distance = hypot(point1[0]-point2[0],point1[1]-point2[1])
distance = ((point1[0]-point2[0])**2 + (point1[1]-point2[1])**2)**(1./2)
print(f'distance: {distance}')
'''

# В институте биоинформатики по офису передвигается робот. Недавно студенты из группы программистов написали для него программу, по которой робот, когда заходит в комнату, считает количество программистов в ней и произносит его вслух: "n программистов". Для того, чтобы это звучало правильно, для каждого nn нужно использовать верное окончание слова. Напишите программу, считывающую с пользовательского ввода целое число nn (неотрицательное), выводящее это число в консоль вместе с правильным образом изменённым словом "программист", для того, чтобы робот мог нормально общаться с людьми, например: 1 программист, 2 программиста, 5 программистов. В комнате может быть очень много программистов. Проверьте, что ваша программа правильно обработает все случаи, как минимум до 1000 человек.
'''
num_string = input("введите кол-во человек: ") 
num = int(num_string)
string = "программист"
end1 = ""
end2 = "а"
end3 = "ов"
if 11 <= num <=14:
    print(f'{num} {string+end3}')
else:
    if len(num_string)>=3:
        x= num%100     
    else:
        x=num%10         
    if 11 <= x <=14:
        print(f'{num} {string+end3}')
    else:
        y=x%10
        if y==0 or 5<=y<=9:
            print(f'{num} {string+end3}')
        elif 2<=y<=4:  
            print(f'{num} {string+end2}')
        else:
            print(f'{num} {string+end1}')
            
'''
#КНБ - вы играете с ботом, варианты раунда игры - победа 1 очко, проигрыш 0 очков, ничья 0.5 балла, чтоб статистика сохранялась, и можно было играть неограниченное количество раундов

p_score = 0
b_score = 0

while True:
    num1 = int(input("введите число (1- камень, 2 - ножницы, 3 - бумага):  "))
    from random import randint
    num2 = randint(1, 3)
    if num1 == 1 and num2 ==1:
        p_score+=0.5
        b_score+=0.5
        print(f"no win (player:{p_score}, bot:{b_score})")
    elif num1 == 1 and num2 == 2:
        p_score+=1
        print(f"player win (player:{p_score}, bot:{b_score})")
    elif num1 == 1 and num2 == 3:
        b_score+=1
        print(f"computer win (player:{p_score}, bot:{b_score})")
    elif num1 == 2 and num2 == 2:
        p_score+=0.5
        b_score+=0.5
        print(f"no win (player:{p_score}, bot:{b_score})")
    elif num1 == 2 and num2 == 1:
        b_score+=1
        print(f"computer win (player:{p_score}, bot:{b_score})")
    elif num1 == 2 and num2 == 3:
        p_score+=1
        print(f"player win (player:{p_score}, bot:{b_score})")

    elif num1 == 3 and num2 == 3:
        p_score+=0.5
        b_score+=0.5
        print(f"no win (player:{p_score}, bot:{b_score})")
    elif num1 == 3 and num2 == 2:
        b_score+=1
        print(f"computer win (player:{p_score}, bot:{b_score})")
    elif num1 == 3 and num2 == 1:
        p_score+=1
        print(f"player win (player:{p_score}, bot:{b_score})")
    else:
        print("введите число от 1 до 3")

    ask = input('еще партию? Введите: +/- ')
    if ask !="+":
        break
