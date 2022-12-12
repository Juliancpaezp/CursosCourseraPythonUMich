# 5.2 Write a program that repeatedly prompts
# a user for integer numbers until the user
# enters 'done'. Once 'done' is entered, print
# out the largest and smallest of the numbers.
# If the user enters anything other than a valid
# number catch it with a try/except and put out
# an appropriate message and ignore the number.
# Enter 7, 2, bob, 10, and 4 and match the
# output below.
# Invalid input
# Maximum is 10
# Minimum is 2

largest = None
smallest = None

while True:
    num = input("Enter a number: ")

    if num == "done":
        # Formatting variables to desired input
        try:
            largest = int(largest)
            smallest = int(smallest)
        except:
            print("No numbers inputed")
        break

    # Verify if 'num' is really a number
    try:
        num = int(num)
    except:
        print("Invalid input")
        continue

    # Assining largest and smallests its first values
    if largest == None:
        largest = num
    if smallest == None:
        smallest = num

    # Is it the largest?
    if num > largest:
        largest = num

    # Is it the smallest?
    if num < smallest:
        smallest = num

print("Maximum is",largest)
print("Minimum is",smallest)
