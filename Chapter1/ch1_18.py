name = "Josh Jordan"
print(name.replace("Josh", "Kyle")) # Kyle Jordan

#split
sentence = "Today is a good day"
print(sentence.split()) # ['Today', 'is', 'a', 'good', 'day']
print(sentence.split("a")) # ['Tod', 'y is ', ' good d', 'y']

#list to string 也是一個type casting
sentence = "Today is"
print(list(sentence)) # ['T', 'o', 'd', 'a', 'y', ' ', 'i', 's']
