# l_add = lambda x, y: x + y

numbers = [4, 123, 33, 232, 25443]
letters = ['a', 'c', 'f', 'x']
players = [{"first_name": "Alex",
                "last_name": "Buzias",
                "rank": 1},
               {"first_name": "Ioachim",
                "last_name": "Popica",
                "rank": 3},
               {"first_name": "Vasile",
                "last_name": "Ureche",
                "rank": 5
                }]


sorted_numbers = sorted(numbers)
print(sorted_numbers)
print(sorted(letters))
print(sorted([players]), lambda p: p["first_name"])

# map
# filter
# zip

