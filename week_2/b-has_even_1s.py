num = int(input('Enter any decimal number : '))
no_of_1s = bin(num).count('1')

if no_of_1s % 2 == 0:
    print(f'The number of 1s in {num} is even')
else:
    print(f'The number of 1s in {num} is odd')
