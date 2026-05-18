n = int(input())           
s = input().strip() 

# # if the first item and the last item are diff, taking the first item might work so just print 1
# # if no split satisfies the condition, print -1

# if s[0] != s[-1]:
#     print(1)
# else:
#     possible = False


# # then check the other all possible splits
# #  for each split if the number of L and O's in the prefix differs from the suffix, print that split

#     for k in range(1, n):
#         left = s[:k]
#         right = s[k:]

#         if left.count('L') != right.count('L') and left.count('O') != right.count('O'):
#             print(k)
#             possible = True
#             break

#     if not possible:
#         print(-1)

# removerd the part where I just return 1...

Possible= False

for k in range(1, n):
    left = s[:k]
    right =s[k:]
    
    if left.count('L') != right.count('L') and left.count('O') != right.count('O'):
        print(k)
        Possible = True
        break

if not Possible:
    print(-1)