# Finding Armstrong Number accordingt to user input
number = input("Please enter a positive integer :")
num_length = len(number)
total = 0  # it is storage for adding process
if number.isdigit():
    for character in number:
        total += int(character) ** num_length
    if total == int(number):
        print("Your number is Armstrong Number")
    else:
        print("Your number is not Armstrong Number")
else:
    print(" Don't use non-numeric, float, or negative values!")