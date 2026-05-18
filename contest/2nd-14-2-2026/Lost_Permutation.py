t = int(input())

for i in range(t):
    m, s = map(int, input().split())
    b = list(map(int, input().split()))
    
    used = set(b)
    
    if len(used) != m:
        print("NO")
        continue
    
    current_sum = sum(b)
    target = current_sum + s
    
    k = 1
    total = 0
    
    while total < target:
        total += k
        k += 1
    
    if total != target:
        print("NO")
        continue
    
    # Now check if all b elements are inside 1..k-1
    valid = True
    for x in b:
        if x >= k:
            valid = False
            break
    
    print("YES" if valid else "NO")
