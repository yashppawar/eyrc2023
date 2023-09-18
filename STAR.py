# cook your dish here

def stars_in_our_pattern(n):
    for i in range(n, 0, -1):
        for j in range(1, i + 1):
            print('#' if (j % 5) == 0 else '*', end="")
        
        print()

n_test_cases = int(input())

for _ in range(n_test_cases):
    n = int(input())
    stars_in_our_pattern(n)
    
