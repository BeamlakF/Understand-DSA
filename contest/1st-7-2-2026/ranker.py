n = int(input().strip())
a = list(map(int, input().split()))

res = []
for i in range(n):
    count = 0
    for j in range(n):
        if a[j] > a[i]:
            count += 1
    res.append(count + 1)

print(*res)

# 5 has no value greater that it, so count = 0 + 1
# 4 has 2 values greater, so count = 2 + 1