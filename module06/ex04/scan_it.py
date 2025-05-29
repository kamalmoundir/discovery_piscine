#!/usr/bin/env python3

import sys
import re

if(len(sys.argv) == 3):
    result = re.findall(sys.argv[1], sys.argv[2])
    if len(result) != 0:
        print(len(result))
    else:
        print("none")
else:
    print("none")