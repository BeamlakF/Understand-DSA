import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n, k = map(int, input().split())    
    #b, c = map(int(input().split()))

    #count = 0, I thought keeping the count and then comparing it with n, but how would that help?
    # I need sth to keep the cost and brand as a key and value ...intead of a list...I would need a dict
    # That resulted in TLE, so Counter maybe? Counter didn't work so can i populate a new list as not to get TLE, and for it not to go over k?
    mylist = [0] * (k + 1)
# I know it's greedy because we have to assign the big amounted ones in the shelves first, 
# but what other algorthm can help me find the biggest cost with the same brand?
# how can i access b anc tho if they are in k...
    for _ in range(k):
        b, c = map(int, input().split())    
# Can I sort it so that I can get the biggest one first,

# I got TLE-

        # if b in mydict:
        #     mydict[b] += c
        # else:
        #     mydict[b] = c
        mylist[b] += c

#I got it again !
    # values = list(mydict.values())
    # values.sort(reverse=True)

    # then how do I do this without sorting as not to get TLE,
    n_sum = 0
    count = 0
    for value in sorted(mylist, reverse=True):
        if value > 0:
            n_sum += value
            count += 1
            # I knew I needed sth to keep n in check!
            if count == n:
                break

    print(n_sum)