'''
Задайте натуральное число N. 
Напишите программу, которая составит список простых множителей числа N.
'''
number = int(input('Введите натуральное число: '))
arr = []
a = 2
while a <= number:
    if number % a == 0:
        arr.append(a)
        number = number / a
    else:
        a += 1
print(arr)

    