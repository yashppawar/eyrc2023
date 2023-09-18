# Input the number of test cases
T = int(input())

# Iterate through each test case
for _ in range(T):
    N = int(input())  # Number of students in the class
    
    # Initialize variables to keep track of maximum score and names
    max_score = -1.0
    max_score_names = []

    # Read student names and scores and find the maximum score
    for _ in range(N):
        student_name, score = input().split()
        score = float(score)  # Convert score to float
        
        # Check if the current student has a higher score
        if score > max_score:
            max_score = score
            max_score_names = [student_name]
        elif score == max_score:
            max_score_names.append(student_name)

    # Sort the names in ascending alphabetical order
    max_score_names.sort()

    # Print the names of students with the maximum score
    for name in max_score_names:
        print(name)
