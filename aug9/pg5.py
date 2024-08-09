t=(11,222,332,4,21,4,99)
t1 = sorted(t) # sorted give you list
t2 = sorted(t,reverse=True)
print(t.count(222))
print(t1)
print(t2)
t3 = tuple(sorted(t))
print(t3)