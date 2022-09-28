# 3-Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между
# максимальным и минимальным значением дробной части элементов.
# Пример:
# [1.1, 1.2, 3.1, 5.17, 10.02] => 0.18 или 18
# [4.07, 5.1, 8.2444, 6.98] - 0.91 или 91

# import random
import math

# Первый #
list1 = [1.1, 1.2, 3.1, 5.17, 10.02]
# list1 = [4.07, 5.1, 8.2444, 6.98]
list1_new = []
for i in list1:
    list1_new.append(round((i-math.floor(i)), 10)) # округление в меньшую сторону
print(list1_new)

print(f'Dif = {round(max(list1_new)-min(list1_new), 10)}')

# Второй # 
list1new = []
for i in list1:
    list1new.append(str(i).split(".")[1]) 
max_len1 = len(max(list1new, key=len)) 
for i in range(len(list1new)): 
    list1new[i] = int(list1new[i].ljust(max_len1, "0"))
dif1 = int(str(max(list1new)-min(list1new)).rstrip("0")) 

print("Dif =", dif1)