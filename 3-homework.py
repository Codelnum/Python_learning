# 1. Задайте список. Напишите программу, которая определит, присутствует ли в заданном списке строк некое число.
import random
import string


list_length = int(input("введите длину списка:  ")) 
word_length = 3
letters = string.ascii_lowercase

def get_list(length, n):
    list = []
    for i in range(1, length+1):
        list.append(''.join(random.choice(letters) for i in range(n)))
        i+=1
    return list
gen_list = (get_list(list_length,word_length))

print(gen_list)
x = "".join(random.choice(letters))

print(f'Ищем букву "{x}":')

def find_second_match(list, letter):
    count=0
    for (index,i) in enumerate(list):
        if letter in i:
            count+=1
            if count ==2:
                ind=index
                break
        else: 
            ind=count
    return ind

value = (find_second_match(gen_list, x))
print (value)
if value == 0:
    print(f"Нет такой буквы")
elif value!=0 and value <2:
    print("Нет второго вхождения")
else:
    print(f"Индекс второго вхождения:{value}")









