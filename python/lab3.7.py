f= open(r'C:\Users\User\Desktop\python\test.txt','r')
lines=f.readlines()
y=[]
for x in lines:
    y.append(x)
print(y)
