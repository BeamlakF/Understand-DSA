# n = int(input())
# a = list(map(int, input().split()))


# for i in range(1, n+1):
#     if i not in a:
#         print (i)

n = int(input())
a = list(map(int, input().split()))

a_set = set(a)

for i in range(1, n + 1):
    if i not in a_set:
        print(i)