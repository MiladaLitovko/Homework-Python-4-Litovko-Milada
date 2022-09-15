'''
Даны два файла, в каждом из которых находится запись многочлена. 
Задача - сформировать файл, содержащий сумму многочленов.
'''

with open('first_file_from_Task5.txt') as first_file:
    first_part = first_file.read()

with open('second_file_from_Task5.txt') as second_file:
    second_part = second_file.read()

a = first_part.split(' = ')[0]
b = second_part.split(' = ')[0]

a = a.split(' + ')
b = b.split(' + ')
print(a)
print(b)

res = ''
flag = True
last_a = 0
last_b = 0

if 'x' not in a[-1]:
    last_a = a[-1]
    a.pop()

if 'x' not in b[-1]:
    last_b = b[-1]
    b.pop()

if a[0][-1] < b[0][-1]:
    (a, b) = (b, a)

for i in a:
    for j in b:
        if i[-1] < j[-1]:
            res += j + ' + '
            b.remove(j)
        if i[-1] == j[-1]:
            flag = False
            extI = i.split('*')
            extJ = j.split('*')
            res += str(int(extI[0]) + int(extJ[0])) + '*' + extI[1] + ' + '
            b.remove(j)
    if flag:
        res += i + ' + '
    flag = True

sum = int(last_a) + int(last_b)
plus = ""
if sum != 0:
    plus = f'+ {sum}'

new_file_from_Task5 = open('new_file_from_Task5.txt','w')
new_file_from_Task5.write(res[:-2] + plus + " = 0")
new_file_from_Task5.close()             



