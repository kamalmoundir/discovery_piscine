#!/usr/bin/env python3
import sys

def downcase_it(word):
    return word.lower()

if(len(sys.argv) > 2):
    for n in sys.argv :
        print(downcase_it(n))
else:
    print("none")



