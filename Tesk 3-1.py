# 1- Задайте список из нескольких чисел. Напишите программу, 
# которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# Пример:
# [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

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
n1 = controlNumber()
list1 = []
ListAmount(list1, n1)
print(list1)
Sum1 = 0
for i in range(len(list1)):
    if i%2 != 0:
        Sum1 += list1[i]
print('Sum =', Sum1)