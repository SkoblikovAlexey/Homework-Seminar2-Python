# Задайте список из n чисел последовательности $(1+\frac 1 n)^n$ и выведите на экран их сумму.

Number = int(input('Введите число N: '))
num_sum = 0
result = {}
for key in range(1, Number+1):
    result[key] = round((1 + 1 / key) ** key, 2)
    num_sum += result[key]

print(result, f'\nсумма = {num_sum}')
