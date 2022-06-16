# Напишите программу, которая будет преобразовывать десятичное число в двоичное.

num_10 = int(input('Введите десятичное число: '))
num_2 = ''
temp = num_10
while temp > 0:
    num_2 = str(temp % 2) + num_2
    temp = temp // 2
print(num_10, '->', num_2)
