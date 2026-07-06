#和離散數學有關的內建方法  
#交集intersection 集合差 difference  聯集 union
# A = {1,3,4,5}  B = {3,4,7,8} ,A-B = {1,5}, A^B = {3,4}   

a = {1,3,4,5}
b = {3,4,7,8}
print(a.difference(b)) # {1,5}
print(b.difference(a)) # {7,8}
print(a.intersection(b)) # {3,4}
print(a.union(b)) #{1, 3, 4, 5, 7, 8}

#isdisjoint==是否是沒有交集  True or False
print(a.isdisjoint(b)) # False 

# a的元素都在b裡面 則a就是b的子集合subset()  b是母集合superset()
print(a.issubset(b)) # False  