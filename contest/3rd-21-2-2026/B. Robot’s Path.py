# x, y = map(int, input().split())
# s = input().strip()

# for i in range(x):
#     if i + y < x and s[i] == '#' and s[i+y] == '#':
#         print('NO')
#     elif i + y < x and s[i] == '.' and s[i+y] == '.':
#         print('YES')
#         break


# # for i in range(x):
# #     if s[i] == '#'and i+y == '#':
# #         print ('NO')

n, k = map(int, input().split())
s = input().strip()

reach = 0 

for i in range(1, n):
    if s[i] == '.' and i - reach <= k:
        reach = i
    elif i - reach > k:
        print("NO")
        break
else:
    if reach == n - 1:
        print("YES")
    else:
        print("NO")