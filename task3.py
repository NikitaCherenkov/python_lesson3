# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.

def decimal(n):
    dec = divmod(n, 1)
    return round(list(dec)[1], 10)

list_entry = [1.1, 1.2, 3.1, 5, 10.01]
dec_list = []
for i in range(len(list_entry)):
    if decimal(list_entry[i]) > 0:
        dec_list.append(decimal(list_entry[i]))
print(list_entry, '=>', max(dec_list) - min(dec_list))
