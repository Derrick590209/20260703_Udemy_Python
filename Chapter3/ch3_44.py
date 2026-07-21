# for variable in iterable:
#     do something
for letter in "Hello World":
    if letter == letter.upper():
        print(letter) # H w

# a list of tuples
for a, b in [(1,2), (3,5), (5,7)]:# tuple on packing
    print(a+ b) # 3, 8, 12

for tuple in [(1,2), (3,5), (5,7)]:#不好看的懂
    print(tuple[0]+ tuple[1]) # 3, 8, 12

# dictionary (keys)
myDictionary = {"name":"Wilson", "age": 25}

for item in myDictionary:
    print(item) # name   
                # age
for item in myDictionary.values():
    print(item) # Wilson   
                # 25
for key, value in myDictionary.items(): # return a list of tuples
    print(f"The key is {key}") # The key is age
    print(f"The value is {value}") # The value is 25

