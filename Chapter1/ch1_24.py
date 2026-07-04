person = {"name": "Wilson", "age": 30}
print(person["name"]) # Wilson
print(person["age"]) # 30
print(person) # {'name': 'Wilson', 'age': 31}

# What data types can be used as dictionary keys?
# In Python, dictionary keys can be of any immutable data type
#What data types can be used as dictionary values?
# Dictionary values can be of any data type, including mutable types like lists and other dictionaries
person = {"x":{"age":[10,20,30]}}
print(person["x"]["age"][1]) # 20


x= {}
x["name"] = "Grace"
x["age"] = 26
print(x) # {'name': 'Grace', 'age': 26}
x["name"] = "Wilson"
print(x) # {'name': 'Wilson', 'age': 26} 
# 所以字典是mutable,但不能修改key,也不能有重複的key
