#!/usr/bin/env python3

num_arr = [2, 8, 9, 48, 8, 22, -12, 2]

print("Original array: ",end = " ")
print(num_arr)

num_arr = [n for n in num_arr if n > 5]
i = 0

for n in num_arr:
    if n > 5:
        num_arr[i] = n + 2
    i += 1
    
print("New array: ",end = " ")
print(num_arr)


