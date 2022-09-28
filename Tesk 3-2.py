# 2-Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# [2, 3, 4, 5, 6] => [12, 15, 16];
# [2, 3, 5, 6] => [12, 15]


import random
# import math

def controlNumber():
    while True:
        try:
            n = int(input())
            break
        except:
            continue
    return n

def ListAmount(some_list, n):
    for i in range(n):
        some_list.append(random.randint(0,30))

print("Введите количество элементов списка:")
n2 = controlNumber()
list2 = []
ListAmount(list2, n2)
print(list2)
list2_new = []

while len(list2) != 0:
    if len(list2) == 1:
        list2_new.append(list2[0]**2)
        break
    else:
        a2 = list2.pop(0)
        b2 = list2.pop()
        list2_new.append(a2*b2)
print(list2_new)