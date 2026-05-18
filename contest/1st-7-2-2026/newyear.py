n = int(input())
s = input().strip()

if "2025" not in s:
    print(0)
else:
    ans = 10**9
    for i in range(n - 3):
        cost = 0
        if s[i] != '2': cost += 1
        if s[i+1] != '0': cost += 1
        if s[i+2] != '2': cost += 1
        if s[i+3] != '6': cost += 1
        ans = min(ans, cost)

    print(ans)




