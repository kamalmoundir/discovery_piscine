#!/usr/bin/env python3

print("Enter the first number:")
nbr1 = int(input())

print("Enter the second  number:")
nbr2 = int(input())
mult = nbr1 * nbr2
print (str(nbr1) + " x " + str(nbr2) + " = " + str(mult))

if mult > 0:
 print("This number is positive.")
elif mult < 0:
 print("This number is negative.")
else :
 print("This number is both positive and negative.")
