#!/usr/bin/env python3



def add_one(num):
    num += 1
    print(f"variable in add_one {num}")
    return num

var = 10

print(f"variable befor add_one called {var}")

add_one(var)

print(f"variable after add_one called {var}")