#!/usr/bin/env python3

num_arr = [2, 8, 9, 48, 8, 22, -12, 2]

print(num_arr)

num_arr = [n for n in num_arr if n > 5]
i = 0


my_set = set()
for n in num_arr:
    if n not in my_set:
        my_set.add(n)
update_set = set()
for n in my_set:
    if n <= 5:
        update_set.add(n)
    else:
        update_set.add(n + 2)

print(update_set)