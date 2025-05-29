#!/usr/bin/env python3

def greetings(word=None):
    if word == None:
        print("Hello, noble stranger.")
    elif isinstance(word ,str):
        print(f"Hello, {word}.") 
    else:
        print("Error! It was not a name.")

greetings('Alexandra')
greetings('Wil')
greetings()
greetings(42)
