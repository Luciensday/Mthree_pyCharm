t=(77)
print(t, type(t))


t=(77,)
print(t, type(t))

t=(11,22,33,44)
for i in range(len(t)):
      print(t[i], end="\t")
print()
for x in t:
    print(x, end="\t")