"""
============
AND
============
con1  con2  result
true  true  true
true  false  false


=============
OR
=============
Con1  Con2  result
True   True  True
True   False  True
False  True   True
False  False  False
"""


"""
Accept 3 input marks from the User
m1 m2 and m3
find the total 
find the average 
find the max marks among 3 input given 
"""

m1 = int(input("mark 1: "))
m2 = int(input("mark 2: "))
m3 = int(input("mark 3: "))

total = m1 + m2 + m3
average = total / 3

max = 0
if m1 > m2 and m1 > m3:
    max = m1
elif m2 > m3 and m2 > m1:
    max = m2
elif m3 > m1 and m3 > m2:
    max = m3

print(total, average, max)