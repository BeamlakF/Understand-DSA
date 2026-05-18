t = int(input())

for i in range(t):
    n = int(input())
    s = input().strip()
    
    seen = set()
    possible = False
    
    for i in range(n - 1):
        sub = s[i:i+2]  
        if sub in seen:
            possible = True
            break
        
        if i > 0:
            seen.add(s[i-1:i+1])
    
    print("YES" if possible else "NO")
