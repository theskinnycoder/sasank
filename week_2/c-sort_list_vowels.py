def get_no_of_vowels(word):
    count = 0
    for letter in word:
        if letter in 'aeiou':
            count += 1
    return count

arr = input("Enter a list of words: ").split()

arr.sort(key=get_no_of_vowels, reverse=True)
print(arr)
