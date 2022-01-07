string = input("Enter a string: ")

letter_freq = {}

for letter in string:
    if letter in letter_freq:
        letter_freq[letter] += 1
    else:
        letter_freq[letter] = 1

sorted_chars = sorted(letter_freq.keys(), key=letter_freq.get, reverse=True)

output = []
for char in sorted_chars:
    output.append((char, letter_freq[char]))

print(output)
