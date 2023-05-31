# 1 - створити функцію яка виводить ліст
from random import random, randint


def print_list(data):
    print(data)


lst = 1, 7, 3, 8
print_list(list(lst))


# 2 - створити функцію яка приймає три числа та виводить та повертає найбільше.
def get_max_print_max(one: int | float, two: int | float, three: int | float):
    res = (max(one, two, three))
    print(f'2.1. args: {lst[0:3]} max: {res}')
    return res


print(f'2.2 args: {lst[0:3]} max: {get_max_print_max(*lst[0:3])}')


# 3 - створити функцію яка приймає будь-яку кількість чисел, повертає найменьше, а виводить найбільше
def get_min_print_max(*args: int | float):
    print(f'3.1. args: {args} max: {max(args)}')
    return min(args)


print(f'3.2 list {list(lst)} min: {get_min_print_max(*lst)}')


# 4 - створити функцію яка повертає найбільше число з ліста

def get_max_list(lst: []):
    return max(lst)


random_lst = [i * randint(0, 5) for i in lst]
print(f'4. random list: {random_lst} max: {get_max_list(random_lst)}')


# 5 - створити функцію яка приймає ліст чисел та складає значення елементів ліста та повертає його.
def get_sum_list(lst: []):
    return sum(lst)


print(f'5. random list: {random_lst} sum: {get_sum_list(random_lst)}')


# 6 - створити функцію яка приймає ліст чисел та повертає середнє арифметичне його значень.

def get_avg_list(lst: []):
    return sum(lst)/len(lst)


print(f'6. random list: {random_lst} avg: {get_avg_list(random_lst)}')
