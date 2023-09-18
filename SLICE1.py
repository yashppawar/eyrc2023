T = int(input())
for _ in range(T):
    n = int(input())
    L = list(map(int, input().split()))
    print(*L[::-1])
    print(*[L[i]+3 for i in range(3, n, 3)])
    print(*[L[i]-7 for i in range(5, n, 5)])
    print(sum(L[3:8]))
