# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

def fibonacci(n):
    if n in (1, 2):
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)

input_number = int(input('Задайте число: '))
fibonacci_list = []
temp = []
for i in range(1, input_number + 1):
    temp.append(fibonacci(i))
for i in range(0, len(temp)):
    if (len(temp) - i) % 2 == 0:
        fibonacci_list.append(0 - temp[len(temp) - 1 - i])
    else:
        fibonacci_list.append(temp[len(temp) - 1 - i])
fibonacci_list.append(0)
for i in range(0, len(temp)):
    fibonacci_list.append(temp[i])
 
print(input_number, '->', fibonacci_list)
