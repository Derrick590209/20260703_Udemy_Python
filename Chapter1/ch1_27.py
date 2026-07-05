myTuple = (10,"100","Hello")
print(len(myTuple)) # 3
print(myTuple[1]) # 100
print(myTuple[0:2])
print(myTuple.count(10)) #1
print(myTuple.index("Hello")) # 2

# Tuples are immutable, so the following line will raise an error
# myTuple[1] = "100" ==  This will raise a TypeError