slow = head
fast = head

while fast and fast.next:
    slow = slow.next       # move 1 step
    fast = fast.next.next  # move 2 steps