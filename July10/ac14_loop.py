'''
Write a script that calculates the lowest common multiple of two given integers.

For example, given the values 4 and 6, the lowest common multiple is 12.


'''

#dcg is
def gcd(a, b):
    while b != 0 :
        temp = a
        a = b
        b = temp % b
    return a

def lcm(a, b):
    return abs(a * b) // gcd(a, b)

if __name__ == "__main__":
    try:
        num1 = int(input("Enter the first integer: "))
        num2 = int(input("Enter the second integer: "))
        print(f"The lowest common multiple of {num1} and {num2} is {lcm(num1, num2)}")
    except ValueError:
        print("Please enter valid integers.")