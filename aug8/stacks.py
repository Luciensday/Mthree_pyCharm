max = 5
s=[None] * max
top = -1
print(s)

def push():
    global top
    if top == max-1:
        print("Stack overflow")
    else:
        ele = int(input("Enter the ele= "))
        top+=1
        s[top] = ele

def pop():
    global top
    if top == -1:
        print("stack underflow")
    else:
        print(f"Deleting..{s[top]}")
        s[top] = 'none'
        top-=1
def display():
    if top == -1:
        print("Stack empty")
    else:
        print("Stack elements")
        for i in range(top,-1, -1):
            print(s[i])
while True:
    ch = int(input("Enter 1 PUSH Enter 2 POP 3 Display 4 Exit"))

    if ch==1:
        push()
    elif ch==2:
        pop()
    elif ch==3:
        display()


