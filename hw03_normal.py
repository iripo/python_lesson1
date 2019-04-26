# Задание-1:
# Напишите функцию, возвращающую ряд Фибоначчи с n-элемента до m-элемента.
# Первыми элементами ряда считать цифры 1 1

def fibonacci(n,m):
    a = 0
    b = 1
    fiblst = []
 
    for x in range(m):
        if (x < 2):
            fiblst.append(b)
        else:
            a += fiblst[x-1]+fiblst[x-2]
            fiblst.append(a)
        a = 0
    return fiblst [(n-1):m] 

# Задача-2:
# Напишите функцию, сортирующую принимаемый список по возрастанию.
# Для сортировки используйте любой алгоритм (например пузырьковый).
# Для решения данной задачи нельзя использовать встроенную функцию и метод sort()


def sort_to_max(origin_list):
    for i in range(len(origin_list)):
        j=i+1
        for j in range(len(origin_list)):
            if origin_list[j] > origin_list[i]:
                tmp=origin_list[i]
                origin_list[i] = origin_list[j]
                origin_list[j]=tmp
    return origin_list
sort_to_max([2, 10, -12, 2.5, 20, -11, 4, 4, 0])

# Задача-3:
# Напишите собственную реализацию стандартной функции filter.
# Разумеется, внутри нельзя использовать саму функцию filter.
def filteri(filt_val,origin_list):
    return [el for el in origin_list if el==filt_val]


filteri(4,[2, 10, -12, 2.5, 20, -11, 4, 4, 0])
[4, 4]

# Задача-4:
# Даны четыре точки А1(х1, у1), А2(x2 ,у2), А3(x3 , у3), А4(х4, у4).
# Определить, будут ли они вершинами параллелограмма.

x1=int(input("Введите координату X первой точки "))
y1=int(input("Введите координату Y первой точки "))
x2=int(input("Введите координату X второй точки "))
y2=int(input("Введите координату Y второй точки "))
x3=int(input("Введите координату X третьей точки "))
y3=int(input("Введите координату Y третьей точки "))
x4=int(input("Введите координату X четвертой точки "))
y4=int(input("Введите координату Y четвертой точки "))

if ((x1-x2) == 0 or (x1-x4) == 0 or (x2-x3) == 0 or (x3-x4) == 0 ):
    print("не являются вершинами параллелограмма")
else: 
    k1=abs((y1-y2)/(x1-x2))
    k2=abs((y1-y4)/(x1-x4))
    k3=abs((y2-y3)/(x2-x3))
    k4=abs((y3-y4)/(x3-x4))


if (k1==k3 and k2==k4):
    print("не являются вершинами параллелограмма")
else:
    print("не являются вершинами параллелограмма")