t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    
    max_pages = 0
    for i in range(n - 1):
        pages = a[i] + a[n-1]
        if pages > max_pages:
            max_pages = pages
            
    print(max_pages)