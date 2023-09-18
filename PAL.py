def is_palindrome(s):
    s = s.lower()  
    return s == s[::-1]


t = int(input())


for _ in range(t):
    str = input().strip()
    
    if is_palindrome(str):
        print("It is a palindrome")
    else:
        print("It is not a palindrome")
