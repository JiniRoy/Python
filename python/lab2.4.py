str=input("enter the string ");
count={};
for i in str:
    if i in count:
        count[i]+=1;
    else:
        count[i]=1;
for key in count:
    if count[key]>1:
        print((key,count[key]));
