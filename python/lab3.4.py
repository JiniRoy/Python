f= open(r'C:\Users\User\Desktop\python\test.txt','r')
lines=f.readlines()
n=int(input('enter the lines '))
lastlines= lines[-n: ]
print(lastlines)
