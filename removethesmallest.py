t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    flag = True
    for i in range(1, n):
        if a[i ] - a[i - 1] > 1:
            flag = False
            break
    if flag:
        print("YES")
    else:
        print("NO")
