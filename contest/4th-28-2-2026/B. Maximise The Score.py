# # I midgt have to maitain a sliding window of 2, and then choose the minimum of those 2 number, the length can't be odd because it is 2n


# t = int(input())

# for _ in range(t):
#     n = int(input())
#     arr = list(map(int, input().split()))


#     n = int(2*n)

#     count = 0
#     for i in range (n-1):
#         for j in (i+1, n):
#             count = count + min (arr[i],arr[j])
            

#     print(count)

t = int(input())

for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    
    arr.sort()
    
    count = 0
    for i in range(0, 2*n, 2):
        count += arr[i]
    
    print(count)