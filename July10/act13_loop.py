'''
Activity 13
Write a Python script that computes the frequency of each digit in a given integer.

For example, if the input number is 334, the output should be:

3 occurs 2 times
4 occurs 1 time

'''
print("This programme will tell you the frequency of each digit from your entry number")
userInput = int(input("Enter a number: "))

userInputStr = str(userInput)

frequencyDict = dict()

for i in userInputStr:
    if i in frequencyDict:
        frequencyDict[i] += 1
    else:
        frequencyDict[i] = 1


for key, value in frequencyDict.items():
    print(f'{key} has occured {value} times')




# def digit_frequency(number):
#     # Convert the number to a string to easily iterate over each digit
#     number_str = str(number)
#     # Create a dictionary to store the frequency of each digit
#     frequency = {}
#
#     # Iterate over each character in the string representation of the number
#     for digit in number_str:
#         if digit in frequency:
#             frequency[digit] += 1
#         else:
#             frequency[digit] = 1
#
#     return frequency
#
#
# if __name__ == "__main__":
#     try:
#         # Prompt the user to enter an integer
#         num = int(input("Enter an integer: "))
#         # Compute the frequency of each digit
#         freq = digit_frequency(num)
#         # Print the frequency of each digit
#         for digit, count in freq.items():
#             print(f"{digit} occurs {count} times")
#     except ValueError:
#         print("Please enter a valid integer.")