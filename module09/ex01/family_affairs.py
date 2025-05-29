#!/usr/bin/env  python3

def filter_hair(item):
    name, hair_color = item
    return hair_color == "red"

def find_the_redheads(dict_name):
    result=[]
    filtered_items =dict(filter(filter_hair, dict_name.items()))
    result = list(filtered_items.keys())
    return result

    
dupont_family = {
"florian": "red",
"marie": "blond",
"virginie": "brunette",
"david": "red",
"franck": "red"
}

print(find_the_redheads(dupont_family))