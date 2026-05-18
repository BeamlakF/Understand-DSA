t = int(input())
# Noah is rigging the game , before it even starts
# He will try to make it equal to her by calculating the difference between their picks


for _ in range(t):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))

    a.sort()
    E = 0
    N = 0

    prev = None
    for i, val in enumerate(a[::-1]):  
        if i % 2 == 0:
            E += val
        else:
            earn = min(k, prev - val)
            k -= earn
            N += val + earn

        prev = val
    print(E - N)