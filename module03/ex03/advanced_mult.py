#!/usr/bin/env python3

i = 0
while i <= 10 :
    j = 0
    print("Table of "+str(i)+" : " , end =" ") 
    while j <= 10:
        print( str(i*j)  + " ", end ="")
        j += 1
    print()
    i += 1 