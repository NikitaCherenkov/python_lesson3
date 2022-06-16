# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.

list = input('Введите список чисел через пробел: ').split(' ')
sum = 0
position = 0
for i in range(0, int(len(list) / 2) + 1):
    if position < int(len(list)):
        sum += int(list[position])
    position += 2
print(list, 'Ответ ->', sum)
