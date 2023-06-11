def f(pattern: str):
    try:
        with open('emails.txt', 'r') as file1, open('email_copy.txt', 'w') as file2:
            for i in file1.readlines():
                file2.write(i.split()[-1] + '\n') if pattern in i else False

    except Exception as err:
        print(f'There is an exception {err} happened')


f('@gmail.com')
