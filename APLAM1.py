# cook your dish here
'''
This script is code stub for CodeChef problem code APLAM1_PY
Filename:      APLAM1_PY_solution.py
Created:       27/09/2021
Last Modified: 27/09/2021
Author:        e-Yantra Team
'''

# Import reduce module
from functools import reduce


# Function to generate the A.P. series
def generate_AP(a1, d, n):

    AP_series = []

    # Complete this function to return A.P. series
    for i in range(n):
        AP_series.append(a1 + (i * d))

    return AP_series


def displayList(l):
    for e in l:
        print(e, end=" ")
    print()

# Main function
if __name__ == '__main__':
    
    # take the T (test_cases) input
    test_cases = int(input())

    # Write the code here to take the a1, d and n values
    for _ in range(test_cases):
        a1, d, n = map(int, input().split())
        # print(f"{a1 = }, {d = }, {n = }")

        # Once you have all 3 values, call the generate_AP function to find A.P. series and print it
        AP_series = generate_AP(a1, d, n)
        displayList(AP_series)

        # Using lambda and map functions, find squares of terms in AP series and print it
        sqr_AP_series = list(map(lambda x: x**2, AP_series))
        displayList(sqr_AP_series)

        # Using lambda and reduce functions, find sum of squares of terms in AP series and print it
        sum_sqr_AP_series = reduce(lambda tn, tm: tn + tm, sqr_AP_series)
        print(sum_sqr_AP_series)

