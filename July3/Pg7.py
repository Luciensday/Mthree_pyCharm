'''
armstrong Number

n =153
sum = 0

n   r=n%10  su,=su,+r**3    n=n//3
---------------------------------------
153     3   0+9 = 9         15
15      5   27+125=153      1
1       1   152+1=153       0

'''

n = int(input("Enter the n = "))
sum = 0
orig = n
while n > 0:
    r = n % 10
    sum = sum + r ** 3
    n = n //10
if orig ==sum:
    print("Armstrong num")
else:
    print("Not an Armstrong num")