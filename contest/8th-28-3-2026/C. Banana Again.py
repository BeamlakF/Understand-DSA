n = int(input())
weight =list(map(int, input().split()))

# first I have to find subsets, then measure the subset and then find the difference between each subset and retiurn the smallest disff
# but then how d I divide it eually...the smaller the difff....the more equal maybe????


total = sum(weight)
answer = float('inf')
half_total = total // 2

for i in range(2 ** n//2):
    #from the subset formula because n is not working...say I have a set with 3 elements...my subset is 8 = 2**3
    all_sum = 0

    for j in range(n):
        if i& (2**j):
            all_sum+= weight[j]

    if all_sum > half_total:
        continue

    diff = total - 2 * all_sum
    if diff < answer:
        answer = diff

print(answer)