x = 3 + 4j
y = 5 - 7j
print(x+y) #(8-3j)

def hello():# hello is stored in RAM base 16 
    print("hello")

print(hello) # <function hello at 0x7ad02ddab1a0>
print(hello()) #hello
               #None ===沒有設定return值   

myList = ["a", "b", "c", "d"]
myString = "|".join(myList)
print(myString) # a|b|c|d