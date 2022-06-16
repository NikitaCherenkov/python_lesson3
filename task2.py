# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.

list_entry = input('Введите список чисел через пробел: ').split(' ')
sums = []
dif = 0
if len(list_entry) % 2 != 0:
    dif += 1
for i in range(0, int(len(list_entry) / 2) + dif):
    sums.append(int(list_entry[i]) + int(list_entry[len(list_entry) - 1 - i]))
print(list_entry, '=>', sums)
