#!/usr/bin/env python3
import sys

if(len(sys.argv) > 1):
    print ("parameters: " + str(len(sys.argv) - 1))
    for n in sys.argv[1:] :
        print(n + " : "+ str(len(n)))
else:
    print("none")