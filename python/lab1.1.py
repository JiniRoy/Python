from datetime import date
a=input('enter your name ');
b=int(input('enter your age '));
today=date.today();
year=today.year;
h=year+(100-b);
print('hello '+a+' the year you will turn 100 is ',h);