# Задайте последовательность чисел. Напишите программу, которая выведет список 
# неповторяющихся элементов исходной последовательности.
# Пример:
# - Ввод:[1,1,2,4,5,6,7,7,8], результат: [2,4,5,6,8]

from random import randint
lst = [randint(1,9) for i in range(10)]
print(f"Наш список из рандомных чисел: {lst}") 

def sample(lst):
    d={i: lst.count(i) for i in lst}
    l=[k for k,v in d.items() if v==1]
    print("Список чисел из неповторяющихся элементов: ",end=" ")
    print(l)

sample(lst) 
