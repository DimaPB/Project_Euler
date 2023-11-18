n_numbers = list(range(1, 1000))
new_list = []
for i in n_numbers:
    if i % 3 == 0 or i % 5 == 0:
        new_list.append(i)
print(n_numbers, new_list)
print(sum(new_list))