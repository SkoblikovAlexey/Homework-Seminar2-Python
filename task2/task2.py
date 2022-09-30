# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.

# Пример:

# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

n = int(input("Введите число N = "))

num_list = []

def fact(n):
    if n == 1: return 1
    else: return n * fact(n - 1)

for i in range(1, n + 1):
    num_list.append(fact(i))

print(num_list)