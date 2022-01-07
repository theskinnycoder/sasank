def anagrams(str1, str2):
    str1 = list(str1.lower())
    str2 = list(str2.lower())
    str1.sort()
    str2.sort()

    return str1 == str2

str1 = input("Enter string 1 : ")
str2 = input("Enter string 2 : ")
if anagrams(str1, str2):
    print("The strings are anagrams")
else:
    print("The strings are not anagrams")
