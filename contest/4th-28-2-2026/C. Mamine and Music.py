# n , k = map(int(input()))
# arr = list(map(int, input().split()))

# spots = 0
# n = len(arr)

# for i in range(n):
#     spots = spots + arr[i]

#     for spot in range(k):
#         while k<=spots:
#             spot +=spots

#     print 

n, k = map(int, input().split())
a = list(map(int, input().split()))

index = sorted(range(n), key=lambda i: a[i])

spots = 0
result = []

for i in index:
    if spots + a[i] <= k:
        spots += a[i]
        result.append(i + 1)  
    else:
        break

print(len(result))
print(*result)