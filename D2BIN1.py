def dec_to_binary(n):
    # Base case: If n is 0, return an 8-bit binary string of all zeros.
    if n == 0:
        return '0' * 8
    else:
        # Calculate the binary representation of n // 2 recursively.
        binary = dec_to_binary(n // 2)
        # Append the least significant bit of n (n % 2) to the result.
        binary += str(n % 2)
        
        # Ensure that the binary string is 8 bits by adding leading zeros if needed.
        while len(binary) < 8:
            binary = '0' + binary
        
        # Ensure that the binary string is not longer than 8 bits by removing extra leading zeros.
        if len(binary) > 8:
            binary = binary[-8:]
        
        return binary
        return binary

# Input the number of test cases
T = int(input())

# Iterate through each test case
for _ in range(T):
    n = int(input())
    binary_result = dec_to_binary(n)
    print(binary_result)  # This will print the 8-bit binary representation of the decimal number.
