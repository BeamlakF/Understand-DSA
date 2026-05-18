t = int(input())
for _ in range(t):
    n, m, k = map(int, input().split())
    
# Alice paints the ribbons so the most common color shows up as littly as possible  
# and bob-picks the color that’s already there the most and repaints all the other parts.
    samecolor = (n + m - 1) // m
# bob muct count so...
    need = n - samecolor
  
    if need > k:
        print("YES")
    else:
        print("NO")