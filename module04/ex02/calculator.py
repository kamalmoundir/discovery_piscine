#!/usr/bin/env python3

nbr1 = int(input("Give me the first number: "))

nbr2 = int(input("Give me the second number: "))

print("Thank you!")

print(str(nbr1) +" + " + str(nbr2) +" = "+ str(nbr1 + nbr2))
print(str(nbr1) +" - " + str(nbr2) +" = "+ str(nbr1 - nbr2))
if nbr2 != 0 :
    print(str(nbr1) +" / " + str(nbr2) +" = "+ str(int(nbr1 / nbr2)))
else :
    print ("Math ERROR: division upon 0")
print(str(nbr1) +" * " + str(nbr2) +" = "+ str(nbr1 * nbr2))
