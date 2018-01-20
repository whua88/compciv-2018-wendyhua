def fob(y):
    for i in range(1, y):
        if i % 3 is 0 and i % 5 is 0:
            print(i, '', 'FizzBuzz')
        elif i % 3 is 0:
            print(i, '', 'Fizz')
        elif i % 5 is 0:
            print(i, '', 'Buzz')
        else:
            print(i)