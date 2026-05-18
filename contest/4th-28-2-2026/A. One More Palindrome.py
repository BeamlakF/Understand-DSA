# t = int(input())

# for _ in range(t):
#     s = input()

# k = ""
# n = len(s)
# right = n -1
# count = 0

# for left in range(n):
#     if s[left] == s[right]:
#         continue
     
#     else:
#         count +=1
#     right -=1
    
#     while left < right:
#         k+ s[left] 
#         k+ s[right]
        

# if count<= 1 and k!=s:
#     print ("yes")
# else: print("NO")     

# t = int(input())

# for _ in range(t):
#     s = input().strip()
    
#     if len(set(s)) <= 2:
#         print("NO")
#     else:
#         print("YES")

t = int(input())

for _ in range(t):
    s = input().strip()
    n = len(s)
    
    left = 0
    right = n - 1
    palin = True
    
    while left < right:
        if s[right] != s[0]:
            palin = False
            break
        left += 1
        right -= 1
    
    if palin:
        print("NO")
    else:
        print("YES")