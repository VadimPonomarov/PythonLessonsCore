# 1)Дан list:
#   list = [22, 3,5,2,8,2,-23, 8,23,5]
#   - знайти мін число
#   - видалити усі дублікати
#   - замінити кожне 4-те значення на 'X'

lst = [22, 3, 5, 2, 8, 2, -23, 8, 23, 5]

print(f'List: {lst} min {min(lst)}')
print(f'List: {lst} без дублікатів:  {list(set(lst))}')
print(f'List: {lst} з кожним четвертим X:  {["X" if not ((i + 1) % 4 or i == 0) else v for i, v in enumerate(lst)]}')


# 2) вивести на екран пустий квадрат з "*" сторона якого вказана як агрумент функції

def square_asterics(num: int):
    first_and_last = '* ' + ' * ' * (num - 2) + ' *'
    next = '* ' + '   ' * (num - 2) + ' *'
    for i in range(num):
        print(first_and_last) if (i == 0 or i == (num - 1)) else print(next)


square_asterics(10)


# 3) вывести табличку множення за допомогою цикла while

def multiplication_table():
    line = []
    for i in range(1, 10):
        for j in range(1, 10):
            line.append(f'{(i * j):3}')
        print(' '.join(line))
        line.clear()


print('\n' * 3, 'Таблиця множення', '\n' * 3, '*' * 50)
multiplication_table()
print('*' * 50)


def multiplication_table_():
    i = 1
    while (10 - i):
        print(''.join([f'{(i * j):3}' for j in range(1, 10)]))
        i += 1


multiplication_table_()


def menu():
    input_val = None
    menu_choice = True

    def set_input():
        menu_choice = input('Зробіть свій вибір ... ')
        match menu_choice.strip():
            case "1":
                lst = [22, 3, 5, 2, 8, 2, -23, 8, 23, 5]

                print(f'List: {lst} min {min(lst)}')
                print(f'List: {lst} без дублікатів:  {list(set(lst))}')
                print(
                    f'List: {lst} з кожним четвертим X:  {["X" if not ((i + 1) % 4 or i == 0) else v for i, v in enumerate(lst)]}')
            case "2":
                square_asterics(10)
            case "3":
                print('\n' * 3, 'Таблиця множення', '\n' * 3, '*' * 50)
                multiplication_table()
                print('*' * 50)
                multiplication_table_()
            case _:
                menu_choice = False
                print('There is nothing to do with the data ...')

    def internal():

        while True:
            print('''
            1 - 
            2 -
            3 -
            ''')
            set_input()

    return internal


menu()()
