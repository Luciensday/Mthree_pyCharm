# prime number

n = int(input("Enter the n val =  "))

i = 2
while i < n :
    if n % i ==0:
        print("this is not a prime num= ", n)
        break
    i = i+ 1

else:
    print("this is a prime num =  ", n)