li=[1,2,3,4]
subli=[[]]
for i in range (0,len(li)+1):
    for j in range (i+1,len(li)+1):
        x=li[i:j]
        subli.append(x)
print(subli)


