#!/usr/bin/env python3
import sys

if len(sys.argv) == 3:
    start = int(sys.argv[1])
    end = int(sys.argv[2])
    array = range(start, end +1)
    print(list(array))        
else:
    print ("none")