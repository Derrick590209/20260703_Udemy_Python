# List
friends = ["Wilson", "Mike", "Nelson", "Greg", "Jimmy"]

#append
friends.append("Aaron")
print(friends) # ['Wilson', 'Mike', 'Nelson', 'Greg', 'Jimmy', 'Aaron']
friends.append(15.0)
print(friends) # ['Wilson', 'Mike', 'Nelson', 'Greg', 'Jimmy', 'Aaron', 15.0]

#pop-1
friends = ["Wilson", "Mike", "Nelson", "Greg", "Jimmy"]
my_lost_friend = friends.pop() #預設index=-1,也就是最後一個元素
print(my_lost_friend) # Jimmy
print(friends) # ['Wilson', 'Mike', 'Nelson', 'Greg']

#pop-2
friends = ["Wilson", "Mike", "Nelson", "Greg", "Jimmy"]
my_lost_friend = friends.pop(2) # 移除並返回索引為2的元素
print(my_lost_friend) # Nelson
print(friends) # ['Wilson', 'Mike', 'Greg', 'Jimmy']   

# 好的思考題
x = [1,2,3,4,5,6]
y = x # y=[1,2,3,4,5,6]
y[0] = 15 # y=[15,2,3,4,5,6]
print(x) # [15, 2, 3, 4, 5, 6] ==copy by reference(mutable), x and y point to the same list object
print(y) # [15, 2, 3, 4, 5, 6]

a=10
b=a
b=15
print(a) # 10 ==copy by value(immutable), a and b point to different int objects
print(b) # 15

# copy ==目的是保留x為原始值,不受y的影響
x = [1,2,3,4,5,6]
y = x.copy() # y=[1,2,3,4,5,6]
y[0] = 15 # y=[15,2,3,4,5,6]
print(x) # [1, 2, 3, 4, 5, 6] ==copy by value(mutable), x and y point to different list objects
print(y) # [15, 2, 3, 4, 5, 6].


# List of list
x = [1,2,[3,4,5,],2,1,[4,3,[-10,4]]]
print(x[2]) # [3, 4, 5]
print(x[2][1]) # 4

y=[1,2,3,4,-2,-4,5,6,7,8,9,10]
print(y[len(y)-1]) # 10

