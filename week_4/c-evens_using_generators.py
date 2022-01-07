def evens():
    num = 0
    while True:
        yield num
        num += 2


gen = evens()
print(gen)
for _ in range(10):
    print(next(gen), end=" ")
print()
