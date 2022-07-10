#Принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.
'''
day=int(input('введите число от 1 до 7:  '))
def day_check(a):
    if (day == 6 or day == 7):
        print ("it's weekend")
    elif (day>0 and day<6):
        print ("it's not a weekend")
    else:
        print ('bad day')

day_check(day)
'''
#Принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).
x = int(input('введите координату Х:  '))
y = int(input('введите координату Y:  '))
if (x == 0 and y ==0):
    print('это зеро.')
else:
    def quarter_check(a,b):
        if (a>0 and b>0):
            print('1st quarter')
        elif (a<0 and b>0):
            print('2nd quarter')
        elif (a<0 and b<0):
            print('3rd quarter')
        elif ( a>0 and b<0):
            print('4th quarter')
        elif (a==0 and b!=0):
            print('on axis Y')
        elif(a!=0 and b ==0):
            print('on axis X')
        else:
             print('в астрале')
quarter_check(x,y)