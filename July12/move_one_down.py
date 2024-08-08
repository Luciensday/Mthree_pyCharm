'''
giving
0   1    2   3
11 22   33   44

goal
22 33 44 55


l[1:] + l[0] => doesn't work because l[0] return integre not list
so we also need to slice l[0] so it can be wrapped as list
l[1:} + l[0:1]
'''

'''
# solution 1
l = [11,22,33,44]
print(l[1:] + l[0:1])
'''
l = [11,22,33,44]
temp = l[0]
n = len(l)
for i in range(n - 1):
    l[i] = l[i+1]
else:
    l[n-1] = temp
print(l)