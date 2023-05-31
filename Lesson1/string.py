import re


def task_announcement(func):
    def wrapper(*args, **kwargs):
        if func.__doc__:
            print('*' * 60, '\n', func.__doc__)
        res = func(*args, **kwargs)
        print('*' * 60)
        return res

    return wrapper


@task_announcement
def figures_from_string_1(s):
    '''Функція figures_from_string_1(s:str)
        вибирає зі введеної строки цифри і виводить їх через кому
        :param s (type = string)'''
    l = [i for i in s if i.isdigit()]
    print(f'''
    Приклад: figures_from_string_1("{s}")
    Результат виконання: {','.join(l) if len(l) else print('There is no figures in "st"')}
    ''')


@task_announcement
def figures_from_string_2(s):
    '''Функція figures_from_string_2(s:str)
        вибирає зі введеної строки числа і виводить їх так як вони написані
        :param s (type = string)'''
    l = re.split(r'\D+', s)
    print(f'''
        Приклад: figures_from_string_2("{s}")
        Результат виконання: {' '.join(l).strip()}
        ''')

'''
1)написати прогу яка вибирає зі введеної строки цифри і виводить їх через кому,
наприклад:
st = 'as 23 fdfdg544' введена строка

2)написати прогу яка вибирає зі введеної строки числа і виводить їх
так як вони написані
'''

st = 'as 23 fdfdg544'
figures_from_string_1(st)
figures_from_string_2(st)


