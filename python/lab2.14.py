fruits={'apple','pear','banana','grape','orange'}
x=input("enter the item ")
if x in fruits:
    fruits.remove(x)
    print(fruits)
else:
    print("Not present in the set")
    print('orginal set : ',fruits)
