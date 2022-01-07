num = input('Enter any base 36 number : ')
decimal_equivalent = int(num, 36)
octal_equivalent = oct(decimal_equivalent)[2:]

print(f'The octal equivalent of {num} is : {octal_equivalent}')
