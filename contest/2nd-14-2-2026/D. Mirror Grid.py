t = int(input())

for i in range(t):
    n = int(input())
    grid = [list(input().strip()) for _ in range(n)]
    
    ans = 0
    
    for i in range(n // 2):
        for j in range((n + 1) // 2):
            
            # 4 symmetric cells
            a = grid[i][j]
            b = grid[j][n - 1 - i ]
            c = grid[n - 1 - i][n - 1 - j]
            d = grid[n - 1 - j][i]
            
            ones = (a == '1') + (b == '1') + (c == '1') + (d == '1')
            
            ans += min(ones, 4 - ones)
    
    print(ans)
