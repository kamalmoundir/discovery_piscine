#!/usr/bin/env python3
import sys

if(len(sys.argv) > 1):
    for n in sys.argv[1:] :
        if not n.endswith("ism"):
            print(n + "ism")
else:
    print("none")