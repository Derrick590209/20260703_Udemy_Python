a = ([1,2,3],"Wilson") #一個immutable,一個mutable
# a[0] = "Grace" 這是不可以的
a[0][1] = 100 # 可以嗎? a[0]此時已經是個List  
print(a) # ([1,100,3],"Wilson")  #答案是可以的

#Coclusion:
# if an element in a tuple is mutable, then we can just 
# select the element, and then change it.

# If we want to use a tuple as a dictionary key,
# then all element in the tuple has to be immutable.
# a = ([1,2,3],"Wilson") can't be the key of dictionary


# 練習:
# which one van be key of dictionary:
# 1.15, 2."Bob" 3.("TOM",[14,23,27]) 
# 4.["filename",(15,16)] 5."filename" 6.("filename",25,"extension")
# 答案:1,2,5,6