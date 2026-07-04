# count
string = "Today is a good day"
print(string.count("a")) # 3

#count技巧  
string2 = "Good day is a good day"
#想要用count 找出Good出現的次數,不論大小寫
print(string2.lower().count("good")) # 2

#find==可以找到substring index的位置
print(string2.find("good")) # 12
print(string2.find("bad")) # -1

#startswith==判斷字串是否以某個字串開頭
print(string2.startswith("Good")) # True
print(string2.startswith("bad")) # False
