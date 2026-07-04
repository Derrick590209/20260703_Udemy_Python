# List
'list' object has no attribute 'find'

# insert
friends.insert(2, "Aaron")
print(friends) # ['Wilson', 'Mike', 'Aaron', 'Nelson', 'Greg', 'Jimmy']

# remove
friends.remove("Nelson")
print(friends) # ['Wilson', 'Mike', 'Aaron', 'Greg', 'Jimmy']

#clear
friends.clear()
print(friends) # []

#sort
friends.sort()
print(friends) # ['Aaron', 'Greg', 'Jimmy', 'Mike', 'Wilson']

#reverse
print(friends.reverse()) # ['Wilson', 'Mike', 'Jimmy', 'Greg', 'Aaron']
#也可以用
print(friends[::-1]) # ['Wilson', 'Mike', 'Jimmy', 'Greg', 'Aaron']
