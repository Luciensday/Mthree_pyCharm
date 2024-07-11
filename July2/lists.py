s = []
print(s)
s.append(11)
s.append(12)
s.append(13)
print(s)

#replicaton operator
t =s * 3
print(t)

#concatenation operator
a=[11,22,33,44]
b=[10, 20]
c = a+b
print(c)

#membership operator
m = [11, 22, 33, 44, 55, 66, 77, 88, 99]
print(999 in m)
print(22 in m)

print(999 not in m)
print(22 not in m)

# multi demension  square bracket
u = [11,22,33]
u.append([888,666])

print(u)
print(u[0])
print(u[1])
print(u[2])
print(u[3])
print(u[3][0])

# add two list together

l1 = [11,22,33]
l1.extend([10,20,30])
print(l1)
l1.extend([99,987,444])
print(l1)

# length

list2 = [11,22, 33, 44, 55, 66]

print("total num of element in list", len(list2))

for i in range(len(list2)):
    print(list2[i])

# altr array
l3 = [11,22,33]
for i in range(len(l3)):
    l3[i] = l3[i] + 10
print("new ele = ", l3)

# for x in l
l4 = [11,22,33]

for x in l4:
    x = x + 10
    print("inside loop=", x)

print(l4)

# max min sum
l5 = [11, 22, 11, 22, 33, 44, 11]

print(l5.count(11))
print(max(l5))
print(min(l5))
print(sum(l5))

# sort() !! important sort alter the array
l5.sort()
print(l5)
l5.sort(reverse=True)
print(l5)

l6 = [11, 2, 13, 55]
a = sorted(l6)
b = sorted(l6, reverse=True)
print(a,b,l6)

# index and slice
l7 = [11, 22, 33, 44, 55, 66, 77, 88, 99]
print("l[1:5] = ", l7[1:5])
print("l[::2] = ", l7[::2])
print("l[::-1] = ", l7[::-1])
print("l[-9:-5] = ", l7[-9:-5])
print("l[-1:-5:-1] = ", l7[-1:-5:-1])
print("l[1:-2] = ", l7[1:-2])



