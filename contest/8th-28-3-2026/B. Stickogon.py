from collections import Counter

t= int(input())
for _ in range(t):
    n = int(input())
    sticks = list(map(int, input().split()))

    # take care of edge cases first

    # if n < 3:
    #     print(0)
    #     continue

    # count = 0
    # sticks.sort

    # for i in range(n):
    #     if sticks[i] are equal to eachother and their count is more than 3...increment count..else what?

    freq = Counter(sticks)
    count = 0

    for k in freq.values():
        count += k // 3

    print(count)