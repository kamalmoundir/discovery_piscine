#!/usr/bin/env python3

num_arr = [1,2,3,4,5,7,8,9]

print("Original array: ",end = " ")
print(num_arr)
i = 0

for n in num_arr:
    num_arr[i] = n + 2
    i += 1

print("New array: ",end = " ")
print(num_arr)