#    0   1  2   3   4   5   6
t = (11,22, 33, 44, 55, 66, 77)
#    -7 -6  -5  -4  -3  -2  -1

print(t[:]) #(11, 22, 33, 44, 55, 66, 77)
print(t[2:]) #(33, 44, 55, 66, 77)
print(t[:5]) #(11, 22, 33, 44, 55)
print(t[2:6]) #(33, 44, 55, 66)
print(t[::2]) #(11, 33, 55, 77)
print(t[1:6:2]) #(22, 44, 66)

print(t[::-1]) #(77, 66, 55, 44, 33, 22, 11)
print(t[-1:-6:-2]) #(77, 55, 33)
print(t[1:-2]) #(22, 33, 44, 55)
print(t[5:-6])  # not produce anything #()
print(t[5:-6:-1]) #(66, 55, 44, 33)



"""
# tuple
t = (77,)
print(t, type(t))
# without comma, it's not tuple
t = (77)
print(t, type(t))



t1 = (11,22,33,44)
t2 = (1,2,3)

#concatenation operation
t3 = t1+t2
#Replication operation
t4 = t1*3
print(t3)
print(t4)
#print all the tuple value
for x in t1:
    print(x)
"""