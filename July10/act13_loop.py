def digit_frequency(number):
    # Convert the number to a string to easily iterate over each digit
    number_str = str(number)
    # Create a dictionary to store the frequency of each digit
    frequency = {}

    # Iterate over each character in the string representation of the number
    for digit in number_str:
        if digit in frequency:
            frequency[digit] += 1
        else:
            frequency[digit] = 1

    return frequency


if __name__ == "__main__":
    try:
        # Prompt the user to enter an integer
        num = int(input("Enter an integer: "))
        # Compute the frequency of each digit
        freq = digit_frequency(num)
        # Print the frequency of each digit
        for digit, count in freq.items():
            print(f"{digit} occurs {count} times")
    except ValueError:
        print("Please enter a valid integer.")