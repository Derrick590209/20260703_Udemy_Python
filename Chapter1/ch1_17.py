print(len("Aloha")) # 5

# #object-oriented programming(物件導向的程式語言)
name = "Derrick"
print(name.upper()) # DERRICK
print(name.lower()) # derrick

#重點來了 Pthon的字串是不可變的，意思是說，當你對字串做任何操作時，Python會建立一個新的字串，而不是修改原本的字串。
name = "Wilson"
name.upper()
nickname = name.lower()
print(name)
print(name.upper()) # WILSON
print(nickname)


#也可以直接改寫同一個位置的記憶體
name = "Wilson"
name = name.upper() 
print(name) # WILSON

#method chaining
name = "Wilson"
print(name.upper().isupper()) # True

# index 和_19的find比較  若找的字不在裡面,會報error,而find則會回傳-1
name = "Wilson"
print(name[0]) # W  indexing
print(name.index("W")) # 0 index
print(name.index("on")) # 4 從4開始找on


