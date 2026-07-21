# Nested Loops 巢狀迴圈  
counter = 0 #計數器的意思

for i in "1234":
    for j in "abcd":
        print(i,j)
        counter += 1

print(f"counter is now {counter}")
