input_string = input('Enter any string : ')

count = 0
for char in input_string:
    if "aeiou".count(char) >= 1:
        count += 1

print(f'The number of vowels in {input_string} are : {count}')
