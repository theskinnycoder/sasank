def round_robin(lists):
    longest_len = max(list(map(len, lists)))
    for lst in lists:
        lst.extend([None] * (longest_len - len(lst)))

    ans = []
    for tpl in zip(*lists):
        for char in tpl:
            if char is not None:
                ans.append(char)
    return ans

num = int(input("Enter the number of lists : "))
lists = []
for count in range(num):
    new_list = input(f'Enter the space seperated list number {count + 1} : ').split()
    lists.append(new_list)

print(round_robin(lists))
