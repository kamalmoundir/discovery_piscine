#!/usr/bin/env python3

print("Enter a number less than 25: ")
nbr = int(input())

if nbr < 25:
 while (nbr <= 25):
     print("Inside the loop, my variable is "+ str(nbr))
     nbr += 1
else:
    print("ERROR")
