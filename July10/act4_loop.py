'''
Activity 4
Create a program that starts with a list of strings, identifies all the strings with more than two characters, stores the results in another list, and displays the new list.

For example:
a = ["a", "bc", "rye", "hello", "c", ""]
Output:

["rye", "hello"]

'''

a = ["a", "bc", "rye", "hello", "c", ""]
output = []

for word in a:
    if len(word) >= 3:
        output.append(word)

print(output)
