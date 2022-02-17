import random;
p=random.randint(1,9);
r=int(input('Guess the number '));
if r<p:
    print('too low');
elif r==p :
    print('exactly right');
else:
    print('too high');
