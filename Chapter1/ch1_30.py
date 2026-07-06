mySet = set()
print(mySet) # set()

myList=[1,4,3,2,5,1,5]
mySet = set(myList)
print(mySet) #{1,2,3,4,5}
# 或直接寫 mySet = {1,2,3,4,5}

s=set()
s.add(1)
print(s) #{1}
s.add(2)
print(s) #{1,2}
s.add(2)
print(s) #{1,2} 重複會一樣
s.add(3) 
s.discard(1)
print(s)# {2,3}
s.clear()
print(s) # set()