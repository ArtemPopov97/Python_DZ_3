# 5-Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример:
# для k = 8 список будет выглядеть так:
#    [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

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

def Fibonach(n):
    some_listFib = []
    some_listFibonach = []
    for i in range(0,n):
        if i == 0:
            some_listFib.append(0)
        elif 1 <= i <= 2:
            some_listFib.append(1)
            if i == 1:
                some_listFibonach.append(1)
            if i == 2:
                some_listFibonach.append(-1)
        else:
            some_listFib.append(some_listFib[i-2]+some_listFib[i-1])
            some_listFibonach.append(((-1)**(i+1))*some_listFib[-1])
    
    res = some_listFib.copy()
    while len(some_listFibonach) != 0:
        a1 = some_listFibonach.pop(0)
        res.insert(0, a1)
    return res

print("Введите N:")
n2 = controlNumber()
list5 = Fibonach(n2)
print(list5)