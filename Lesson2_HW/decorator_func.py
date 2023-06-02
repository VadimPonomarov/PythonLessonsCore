def decor(func):
    counter = 0

    def wrapper(*args, **kwargs):
        nonlocal counter
        counter += 1
        func(*args, **kwargs)
        print(f'Counter: {counter}')

    return wrapper


@decor
def func():
    print('Function')


func()
func()
func()
func()