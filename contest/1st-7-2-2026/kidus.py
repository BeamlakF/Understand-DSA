s = input().strip()
n = len(s)
found = False

for i in range(1, n):  
    a, b = s[:i], s[i:]
    if a[0] == '0' or b[0] == '0':
        continue
    if int(b) > int(a):
        print(int(a), int(b))
        found = True
        break

if not found:
    print(-1)
