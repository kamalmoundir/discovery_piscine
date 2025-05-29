#!/usr/bin/env python3

import sys

i = 1

if(len(sys.argv) > 1):
    while(i < len(sys.argv[i])):
        if not sys.argv[i].isnumeric():
            print(sys.argv[i])
            break
        i += 1
else:
    print("none")