#!/usr/bin/env python3

s = input()

for ch in s:
    if ch.isupper():
        print(ch.lower(), end = "")
    elif ch.islower():
        print(ch.upper(),end = "")
    else:
        print(ch, end = "")
        
print(s.swapcase())