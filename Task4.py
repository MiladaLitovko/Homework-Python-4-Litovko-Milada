'''
Задана натуральная степень k. 
Сформировать случайным образом список коэффициентов 
(значения от 0 до 100) многочлена и записать в файл многочлен степени k.

*Пример:* 

- k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0
'''
import random

k = int(input('Введите степень k: '))
result = ''
copy_of_k = k
while k >= 0:
    if copy_of_k == k:
        b = random.randint (1,100)
    else:
        b = random.randint (0,100)
    if b == 0:
        k -= 1
        continue
    elif k == 0:
        part = f'{b}'
    else:
        part = f'{b}*x^{k}'
    result += ' + ' + part
    k -= 1
result += ' = 0'

file_from_Task4 = open('file_from_Task4.txt','w')
file_from_Task4.write(result[3:])
file_from_Task4.close()