try:
    t=(56,33,6,33,7)
    print(t.index(33))
    print(t.index(33,2,5))
    print(t.index(999))
except:
    print("The element doesn't exist")
