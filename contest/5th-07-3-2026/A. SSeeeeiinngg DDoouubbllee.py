from collections import Counter

t =  int (input())


for _ in range(t):
    s = input().strip()
    
    #What is the syntax to double the string??
    double = []
    for char in s:
        double.append(char*2)

    double = ''.join(double)
    
    count = Counter(double)
    
    # I will use two pointers to build palindrome
    n = len(double)
    res = [''] * n # beacuse it saif, it has to be, 2n
    left =0
    right = n - 1
    
    for ch in count:
        while count[ch] > 0:
            res[left] = ch
            res[right] = ch
            left += 1
            right -= 1
            count[ch] -= 2
    
    print(''.join(res))