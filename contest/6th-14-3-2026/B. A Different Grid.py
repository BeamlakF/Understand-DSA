t = int(input())
# I think this is a 2-pointer question, I want to swap the values...I don't want transposing or rotationg...because that might end up in not changinf some numbers...so what I wouls is have 2 pointes and keep swaping or reverse the whole grid
# matrice = [list(map(int, input().split())) for _ in range(n)]

for _ in range(t):
    n, m = map(int, input().split())
# I thought this would be my new list, but I will be using a to make b so...
    a = []
    for _ in range(n):
# Because I need to flatten the list, and traumatixes with TLEs...and also I don't know how to use the .flat thing
        a.extend(list(map(int, input().split())))
# to handle the first testcase, I will do:
    if n * m == 1:
        print(-1)
        continue

# I know all elements are distinct so what if I rotate them;
    b = a[1:] + [a[0]]
# this step is to shift anything by 1, 

    index = 0
    for i in range(n):
        print(*b[index:index+m])
        # to unpack the list, multiply b by m...m, is the column
        index += m


