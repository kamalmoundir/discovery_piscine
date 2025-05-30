#!/usr/bin/env python3

def famous_births(item):
    sorted_items = sorted(item.items(), key=lambda kv: (kv[1]["date_of_birth"], kv[1]["name"]))
    for n in sorted_items:
        print(n[1]["name"] +" is a great scientist born in " +n[1]["date_of_birth"])

women_scientists = {
"ada": { "name": "Ada Lovelace", "date_of_birth": "1815" },
"cecilia": { "name": "Cecila Payne", "date_of_birth": "1900" },
"lise": { "name": "Lise Meitner", "date_of_birth": "1878" },
"grace": { "name": "Grace Hopper", "date_of_birth": "1906" }
}
famous_births(women_scientists)