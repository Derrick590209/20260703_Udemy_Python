# Tuple packing
x = 10,15 
print(x) # (10, 15)
print(type(x)) # <class 'tuple'>

# Tuple unpacking means assing indivisual elements of a tuple to multiple variables.
# x = (a,b,c,d) and y1,y2,y3,y4 = x, meaning y1 = a, y2 = b, y3 = c, y4 = d
# 例如:
x = ("Wilson",25)
print(x[0]) # Wilson  但是element若是1000多項  就會很麻煩 也沒有意義
# 若改成
name,age = x
print(name) # variable names have meaning
print(age)

#另一個例子
a,b = (15,100) # a,b = 15,100也可以
print(a)
print(b)

#題目: x=25,y=35  如何讓y=25,x=35
# 方法一:
x = 25
y = 35
temp = x # tepm=25
x = y # x=35
y = temp # y=25

#第二個方法:
x,y = (25,35)
print(x) # 25
x,y = y,x # 同時做tuple packing y,x=(y,x) 和 tuple unpacking
print(x) #35
