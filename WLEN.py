def count_word_lengths(input_str):
    # Check if the string starts with "@"
    if not input_str.startswith("@"):
        print("String does not start with '@'")
        return

    # Extract the words from the string
    words = input_str[1:].split()

    # Count the length of each word and create a comma-separated string
    word_lengths = [str(len(word)) for word in words]
    result_str = ",".join(word_lengths)

    return result_str


# Read the number of test cases
T = int(input().strip())

# Process each test case
for _ in range(T):
    # Read the input string for the test case
    input_str = input().strip()

    # Count word lengths and print the result
    result = count_word_lengths(input_str)
    print(result)
