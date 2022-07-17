#Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

string= input("введите число:   ")
num_string = ''.join(filter(str.isdigit, string))
print(sum(list(map(int,num_string))))

#Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
# N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

num = int(input("введите число:   ")) 

def get_sum(a):
    list=[]
    n=1
    for i in range(1, num+1):
        n = n*i
        list.append(n) 
    return list

print(get_sum(num))