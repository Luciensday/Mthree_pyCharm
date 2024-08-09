# s = "hi this is just a SAMPLE line"
# print(s.capitalize())
# print(s.upper())
# print(s.lower())
# print(s.title())
# print(s.split())
#
# a=33.833333
# print(f"{a:>10}")
#
# b=33
# print(f"{b:10}")
# print(f"{b:<10}") ## left
# print(f"{b:>10}") ## right
# print(f"{b:^10}") ## center

# a="hey how are you?"
# print(a.startswith("hey"))
# print(a.startswith("hey this"))
# print(a.endswith("ou?"))
# print(a.endswith("ou"))


a="88655"
b="khkjh"
c="hkjf9877"
d="jk:>?"
print(a.isalpha())
print(a.isalnum())
print(a.isdigit())

print(b.isalpha())
print(b.isalnum())
print(b.isdigit())

print(c.isalpha())
print(c.isalnum())
print(c.isdigit())

print(d.isalpha())
print(d.isalnum())
print(d.isdigit())


d = "22jk3:>?2"
spchar = "!@#$%^&*"
alpha_var=""
sp_var=""

dig = ""

for x in d:
    if x in spchar:
        sp_var=sp_var+x
    elif x.isalpha():
        alpha_var=alpha_var+x
    elif x.isdigit():
        dig=dig+x
print(f"special char= {sp_var}, alpha = {alpha_var}, dig={dig} ")

