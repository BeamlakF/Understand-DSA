t = int(input())
# ord and #chr are in-built functions, instead of assigning wach character to numericals and making a dictionary out of them

for _ in range(t):
    w = input()
    p = int(input())

    letter_count = {}
    result = ""
    total_price = 0

    for char in w:
        value = ord(char) - ord('a') + 1
        total_price += value

    for char in w:
        if char not in letter_count:
            letter_count[char] = 0
        letter_count[char] += 1

    for letter_value in range(26, 0, -1):  #to make it in reverse order, to remove as few char as possible
        letter = chr(ord('a') + letter_value - 1)

        while (letter in letter_count and letter_count[letter] > 0 and total_price > p):
            letter_count[letter] -= 1
            total_price -= letter_value


    for ch in w:
        if ch in letter_count and letter_count[ch] > 0:
            result += ch
            letter_count[ch] -= 1

    print(result)