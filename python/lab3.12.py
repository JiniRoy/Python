from tkinter import N
f= open(r'C:\Users\User\Desktop\python\list.txt','w')
list=['apple','pear','mango','pineapple']
for item in list:
    f.write(item+'\n')
f.close()
f= open(r'C:\Users\User\Desktop\python\list.txt','r')
print(f.read())
