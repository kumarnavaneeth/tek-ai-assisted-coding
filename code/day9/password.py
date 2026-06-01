from collections import Counter


# Function to check stable number
def isStable(num):

    # Convert number into string
    num = str(num)

    # Count frequency of digits
    freq = Counter(num)

    # Get all frequency values
    values = list(freq.values())

    # Check if all frequencies are same
    first = values[0]

    for v in values:

        if v != first:
            return False

    return True


# Function to find password
def findPassword(input1, input2, input3, input4, input5):

    numbers = [
        input1,
        input2,
        input3,
        input4,
        input5
    ]

    stable_sum = 0

    unstable_sum = 0

    # Check each number
    for num in numbers:

        if isStable(num):

            stable_sum += num

        else:

            unstable_sum += num

    # Password formula
    password = stable_sum - unstable_sum

    return password


# INPUT
input1 = int(input("Enter number 1: "))
input2 = int(input("Enter number 2: "))
input3 = int(input("Enter number 3: "))
input4 = int(input("Enter number 4: "))
input5 = int(input("Enter number 5: "))

# FUNCTION CALL
result = findPassword(
    input1,
    input2,
    input3,
    input4,
    input5
)

# OUTPUT
print("Password:", result)