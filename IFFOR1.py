# Function to perform the given operations on a value i
def compute_value(i):
    if i == 0:
        return 3
    elif i % 2 == 0:
        return i * 2
    else:
        return i ** 2

# Input the number of test cases
T = int(input())

# Iterate through each test case
for _ in range(T):
    n = int(input())  # Number of values to compute

    # Calculate and print the results for each value from 0 to n-1
    result = [str(compute_value(i)) for i in range(n)]
    print(" ".join(result))  # Join the results as a space-separated string
