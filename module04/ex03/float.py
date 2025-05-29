#!/usr/bin/env python3

nbr = input("Give me a number: ")
nbr = float(nbr)

if(nbr.is_integer()):
    print("This number is an integer.")
else:
    print("This number is a decimal.")