# Задача-1:
# Дан список фруктов.
# Напишите программу, выводящую фрукты в виде нумерованного списка,
# выровненного по правой стороне.

# Пример:
# Дано: ["яблоко", "банан", "киви", "арбуз"]
# Вывод:
# 1. яблоко
# 2.  банан
# 3.   киви
# 4.  арбуз

fruits=["яблоко", "банан", "киви", "арбуз"]
for i, value in enumerate(fruits, 1):
     print("{}. {:>11}".format(i, value))

#или

n=0

fruits=["яблоко", "банан", "киви", "арбуз"]
for i in fruits:
    len(i)
    if len(i) > n:
        n=len(i)


for i, value in enumerate(fruits, 1):
     print("{}. {}".format(i, value.rjust(n)))

# Подсказка: воспользоваться методом .format()


# Задача-2:
# Даны два произвольные списка.
# Удалите из первого списка элементы, присутствующие во втором списке.



fruits=["яблоко", "банан", "киви", "арбуз"]
my_fruits=["яблоко", "арбуз"]
if my_fruits in fruits:
    fruits.remove()
print (fruits)


# Задача-3:
# Дан произвольный список из целых чисел.
# Получите НОВЫЙ список из элементов исходного, выполнив следующие условия:
# если элемент кратен двум, то разделить его на 4, если не кратен, то умножить на два.

import numpy as np
just_numbers=list(np.random.randint(100,size=10))
print(just_numbers)
new_numbers=[]
for i in range(len(just_numbers)):
    if (just_numbers[i]%2==0):
        new_numbers.append(just_numbers[i]/4)
    else:
        new_numbers.append(just_numbers[i]*2)
print(new_numbers)

