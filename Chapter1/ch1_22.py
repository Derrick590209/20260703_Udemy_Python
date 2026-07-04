# List
friends = ["Wilson", "Mike", "Nelson", "Greg", "Jimmy"]

# insert
friends.insert(2, "Aaron")
print(friends) # ['Wilson', 'Mike', 'Aaron', 'Nelson', 'Greg', 'Jimmy']

# remove
friends = ["Wilson", "Mike", "Nelson", "Greg", "Jimmy"]
friends.remove("Nelson")
print(friends) # ['Wilson', 'Mike',  'Greg', 'Jimmy']

#clear
friends = ["Wilson", "Mike", "Nelson", "Greg", "Jimmy"]
friends.clear()
print(friends) # []

#sort
friends = ["Wilson", "Mike", "Nelson", "Greg", "Jimmy"]
friends.sort()
print(friends) # ['Greg', 'Jimmy', 'Mike', 'Nelson', 'Wilson']

#reverse
friends = ["Wilson", "Mike", "Nelson", "Greg", "Jimmy"]
friends.reverse()
print(friends) # ['Jimmy', 'Greg', 'Nelson', 'Mike', 'Wilson']
#也可以用
friends = ["Wilson", "Mike", "Nelson", "Greg", "Jimmy"]
print(friends[::-1]) # ['Wilson', 'Mike', 'Jimmy', 'Greg', 'Aaron']
