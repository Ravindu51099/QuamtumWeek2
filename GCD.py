# Function to calculate the GCD of two numbers using the Euclidean Algorithm
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


# Ask the user how many numbers they want to enter
n = int(input("How many numbers do you want to enter? "))

# Store all numbers in a list
numbers = []

# Get the numbers from the user
for i in range(n):
    num = int(input(f"Enter number {i+1}: "))
    numbers.append(num)

# Calculate the GCD of all numbers
result = numbers[0]

for i in range(1, len(numbers)):
    result = gcd(result, numbers[i])

# Display the result
print("\nNumbers entered:", numbers)
print("The GCD is:", result)