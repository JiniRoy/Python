f= open(r'C:\Users\User\Desktop\python\test.txt','r')
len=0
for x in f.readlines():
    len+=1
print(len)