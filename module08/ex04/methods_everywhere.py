#!/usr/bin/env python3

import sys

def shrink(av:None):
    if av is None :
        print()
    else:
        print(av[:8])

def enlarge(av:None):
    if av is None :
        print()
    else:
        print(av.ljust(8,'Z'))

if len(sys.argv) > 1:
    for n in sys.argv[1:] :
        if len(n) > 8:
            shrink(n)
        elif len(n) < 8:
             enlarge(n)
        else:
            print(n)

else:
    print("none")