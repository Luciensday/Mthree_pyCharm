#
# d = {}
# print(type(d))
# d={1,2,3}  #if without key value pair in curly bracket if will be type set
# print(type(d))
#
# d = set()
#
# d.add(11)
# d.add(22)
# d.add(33)
# d.add(11)
# #ignore the repeat value
# print(d)
#
#
# l=[11,22,33,44,11,22,5]
# s=set(l)
# print(s)
#
# s.update([11,2,5,6,7,90])
# print(s)
#
# t={11,22,33,44,55}
# t.discard(44)
# print(t)
# t.discard(99) #it wont give u error if it's not existed
# print(t)
# '''
# f = {11,22,33,44,55}
# s.remove(44)
# print(s)
# s.remove(99) #it will throw error if it's not existed
# '''
#
# #
# # s = {11, 22, 33, 44, 55}
# # s.clear(22) # to catch up
#


# a={11,22,33,44}
# b = {33,44,55,66}
# c = {44,66,77,88}
#
# a.intersection_update(b,c) #intersection_update will alter a' value
# print(a)
#
# a.intersection(b,c) #intersection will NOT alter a' value
# print(a)



# print(a|b)
# print(a.union(b))
#
# print(a&b)
# print(a.intersection(b))


a = {11,22,33,44}
b={ 33,44,55,66}

print(a-b)
print(b-a)

print(a^b)
