n, k = map(int, input().split())
layers= input()

# I think this is greedy:
# we are looking for the smallest amount of weight we can find- we do that by isolating the heaviest letters( dn't tell z)
# to remove z, y and their heavy friends we sort...and then contraint, if we choose "a", we ca't use it neightburs till a+2
# a+2 means till c, I guess "which is at least two positions after in the alphabet" means that and it used the example
# c, then e...we can't go back to choose a but we remove that problem with soring

layersort= sorted(layers)

weight = {}
alphabet = "abcdefghijklmnopqrstuvwxyz"

for i in range(26):
    weight[alphabet[i]] = i + 1

# to count number of layers added yet, we can't go more than k so may be we compare it eith k later?
count = 0 

#to track the weight we have, we will take the minu=imum ones

total = 0
# to check if the the last chose alphabet was far form the next one by to...sth to cpompare that with too

last = ''

for char in layersort:
    if count == 0:
        total += weight[char]
        last = char
    
        count += 1
    else:
        if weight[char] - weight[last] >= 2:
            total+= weight[char]
            last = char
            
            count +=1

    if count == k:
        break

if count < k:
     print(-1)
else:
    print(total)



