'''
Задайте последовательность чисел. 
Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.
'''
a = [1, 2, 2, 3, 4, 5, 7, 82, 2, 1, 1034, 4]

def unique():
    arr = []
    b = set(a)
    for i in b:
        arr.append(b)
    return(b)

print(unique())