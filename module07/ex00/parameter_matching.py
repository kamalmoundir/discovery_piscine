#!/usr/bin/env python3


import sys
import re

if(len(sys.argv) == 2):
    
    word = input("What was the parameter? ")
    if(word == sys.argv[1]):
        print("Good job!")
    else:
        print("Nope, sorry..")
else:
    print("none")