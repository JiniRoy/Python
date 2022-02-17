f =open(r'C:\Users\User\Desktop\python\new.txt')
flist=f.readlines();
newlist=[]
for s  in flist:
   newlist.append(s.rstrip('\n'))
print(newlist)
