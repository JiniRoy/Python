f= open(r'C:\Users\User\Desktop\python\test.txt','r')
line=f.readlines()
li=[x.strip() for x in line]
print(li)
