# Okay, so I have one pile of n a pile of exactly m.Every time, I can split pile in to 2 

# First things first: if n < m, forget it. As I an't add more, and can onlu split...maybe return False here?
# But if f n == m, then that's good...
# But then how do I check  if I can get m from n by splittin it in to 2
# Well, I split,...can I do 2 ways...one thied and 2 third, and chek which gives me m
# so to try ways we can find m by spltting n n to m, what algorithm is better...if we try thin repeatedly may be recursion

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    def cansplit(n, m):
        if n == m:
            return True
        if n < m:
            return False
        
        if n % 3 != 0:
            return False
        
        return cansplit(n // 3, m) or cansplit(2 * n // 3, m)


    
    if cansplit(n, m):
        print("YES")
    else:
        print("NO")