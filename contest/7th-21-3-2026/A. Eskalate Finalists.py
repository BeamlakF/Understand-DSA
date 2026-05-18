k = int(input())
finalists = list(map(int, input().split()))


# I see pattern for the first and the third test case but I don't understand the second test case:
#test case 1: 28-25=3
#test case 2: 92-25= 67
#test case 3: 23 - 25= -2 -> What does this mean though? So I am thinking if there will be 25 people accepted, 
# and there are 5 of them here, the biggest ranker is 23...meaning we know till 23...may be 24 and 25 peopla may
# may have accepted...so there may be 0 declines.
# so in syntax do I just subtract 25 from the max of the list?

answer = max(finalists) - 25

if answer >= 0:
    print(answer)

if answer <0:
    print (0)

