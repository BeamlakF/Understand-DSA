n, B = map(int, input().split())
a = list(map(int, input().split()))

odd = 0
even = 0
candidate_costs = []

for i in range(n-1):  
    if a[i] % 2 == 0:
        even += 1
    else:
        odd += 1

    if odd == even:
        cost = abs(a[i] - a[i+1])
        candidate_costs.append(cost)

# Sort candidate cut costs ascending
candidate_costs.sort()

total = 0
cuts = 0

for cost in candidate_costs:
    if total + cost <= B:
        total += cost
        cuts += 1
    else:
        break

print(cuts)