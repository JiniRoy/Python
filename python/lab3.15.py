import random
f= open(r'C:\Users\User\Desktop\python\combine.txt','r')
linecount=0
list=[]
for line in f.readlines():
    linecount+=1
    list.append(line)
pos=random.randint(0,linecount-1)
print(list[pos])