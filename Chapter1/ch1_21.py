friends1 = "Mike"
friends2 = "Josh"
friends3 = "Jerry"
print(f"{friends1}, {friends2}, and {friends3} are my friends")

friendList = ["Mike", "Josh", "Jerry"]
print(f"{friendList[0]}, {friendList[1]}, and {friendList[2]} are my friends")
print(len(friendList)) # 3

luckyNumbers = [2, 3, 4, 5, 6, 7, 10]
print(luckyNumbers[0]) # 2
print(luckyNumbers[0:3])# [2, 3, 4]
print(luckyNumbers[1:]) # [3, 4, 5, 6, 7, 10]
print(luckyNumbers.count(10)) #1
print(luckyNumbers.index(5)) # 3
print(luckyNumbers.find(5)) # 'list' object has no attribute 'find'


x=[1,2,3]
y=[2,5,8]
print(x+y) # [1, 2, 3, 2, 5, 8]
print(x*3) # [1, 2, 3, 1, 2, 3, 1, 2, 3]

# List is mutable, meaning you can change its content. For example:
x=[1,2,3]
x[0] = 5
print(x) # [5, 2, 3]
