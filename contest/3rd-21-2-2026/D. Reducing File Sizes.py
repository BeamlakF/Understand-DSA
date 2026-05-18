n, m = map(int, input().split())

files = []
totalA = 0
totalB = 0

for _ in range(n):
    a, b = map(int, input().split())
    files.append(a - b)
    totalA += a
    totalB += b

if totalB > m:
    print(-1)
elif totalA <= m:
    print(0)
else:
    need = totalA - m

    files.sort(reverse=True)

    count = 0
    reduced = 0

    for diff in files:
        reduced += diff
        count += 1
        if reduced >= need:
            print(count)
            break
    else:
        print(-1)