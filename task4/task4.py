# Задайте список из N элементов, заполненных числами из промежутка [-N, N]. 
# Найдите произведение элементов на указанных позициях. Позиции хранятся в файле file.txt в одной строке одно число.
import random
n = int(input("Введите количество элементов списка: "))
def create_new_list(num):
    new_list = []
    for i in range(0, num):
        new_list.append(random.randint(-num, num))
    return new_list

new_list = create_new_list(n)
print(new_list)
multiply = 1
path = 'pos.txt'
data = open(path, 'r')
for line in data:
    multiply *= new_list[int(line.strip()) - 1]
print(multiply)