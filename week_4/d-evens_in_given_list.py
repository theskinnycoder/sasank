nums = list(map(int, input("Enter list of numbers : ").split()))

for num in nums:
    if num % 2 == 0:
        print(num)
