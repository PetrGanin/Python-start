# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями). 
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n — кол-во элементов первого множества. m — кол-во элементов второго множества.
# Затем пользователь вводит сами элементы множеств.
from random import randint
array = [randint(1,10) for i in range(10)]
print(array)
array2 = [randint(1,10) for i in range(10)]
print(array2)
for i in array2:
    if i not in array:
        array.append(i)
print(array)
array.sort()
print(array)
arr = set(array)
print(arr)