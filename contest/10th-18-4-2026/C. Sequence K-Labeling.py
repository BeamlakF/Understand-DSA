from collections import defaultdict

n, k = map(int, input().split())
a = list(map(int, input().split()))

freq = defaultdict(int)
for x in a:
    freq[x] += 1

if max(freq.values()) > k:
    print("NO")
    exit()

print("YES")

labels = [0] * n
last_used = [set() for _ in range(k)]

label = 0

for i in range(n):
    val = a[i]

    while val in last_used[label]:
        label = (label + 1) % k

    labels[i] = label + 1
    last_used[label].add(val)

    label = (label + 1) % k

print(*labels)