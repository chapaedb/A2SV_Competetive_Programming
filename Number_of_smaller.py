input_str = input()
t, n = map(int, input_str.split())

a = list(map(int, input().split()))
b = list(map(int, input().split()))
mp = {}
ans = []
count = 0
left = 0
right = 0

while right < len(b) and left < len(a):
    if a[left] < b[right]:
        count += 1
        left += 1
    else:
        ans.append(count)
        right += 1

while right < len(b):
    ans.append(count)
    right += 1

print(*ans)
