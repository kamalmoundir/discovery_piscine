#!/usr/bin/env python3
import sys

if(len(sys.argv) > 2):
    i = len(sys.argv) - 1
    while(i >= 1):
        print(sys.argv[i])
        i -= 1
else:
    print("none")