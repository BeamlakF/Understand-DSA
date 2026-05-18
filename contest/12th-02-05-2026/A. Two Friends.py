t = int(input())
for _ in range(t):
    n = int(input())
    p = list(map(int, input().split()))
    
    ans = 3 #since I am looking only for the minimum(2), the max can't be greater than 3
    for i in range(n):
        friend = i + 1
        best_friend = p[i]
        
        # Check if two people are each other's best friends. and then...
        # use best_friend - 1, since friend starsted indexing from 1
        if p[best_friend - 1] == friend:
            ans = 2
            break
    
    print(ans)

