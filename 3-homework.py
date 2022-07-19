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
    index=0
    count=0
    for i in list:
        if letter in i:
            count+=1
            if count ==2:
                index = i
    return index

print(find_second_match(gen_list, x))









