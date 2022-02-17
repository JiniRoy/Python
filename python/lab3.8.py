f= open(r'C:\Users\User\Desktop\python\test.txt','r')
length=[]
words=[]
for line in f:
    for word in line.split():
        words.append(word)
        length.append(len(word))
big=length[0]
for x in length:
    if(big<x):
        big=x
print(words[length.index(big)])