from itertools import permutations
vow=['a','e','i','o','u'];
p=permutations(vow);
for i in list(p):
    print(''.join(i))
