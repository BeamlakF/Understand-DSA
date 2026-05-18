n = int(input())
a = list(map(int, input().split()))

a.sort()

l = 0
r = n - 1
ans = 0

while l < r:
    s = a[l] + a[r]
    ans += s * s
    l += 1
    r -= 1

print(ans)