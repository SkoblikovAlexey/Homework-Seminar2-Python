# Реализуйте алгоритм перемешивания списка.
import random
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

def list_shuffle(shuffled_list):    
    random.shuffle(shuffled_list)
    return shuffled_list
print(numbers)
print(list_shuffle(numbers))
