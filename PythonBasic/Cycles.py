#while
#1
i = 1
while i<=10:
    print(i)
    i += 1
    
#2
c = 0
while c<12:
    c += 2
    if c == 4: #skip 4
        continue
    print(c)

#For
#1
names = ["Eugene", "Tokyo", "Anna"]
print(names)
for x in names:
    print(x)
print()   

#2
for x in "hello":
    if x=="l":
        continue #skip "ll"
    print(x)

#3
for y in range(2, 100, 7):
    print(y)
else:
    print("done")
    
        

