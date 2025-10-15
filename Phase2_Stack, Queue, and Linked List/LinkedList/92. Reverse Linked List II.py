class Solution:
    def reverseBetween(self, head: Optional[ListNode], m: int, n: int) -> Optional[ListNode]:
        if not head or m == n:
            return head

        dummy = ListNode(0)
        dummy.next = head
        prev = dummy

        # Step 1: Move prev to node before position m
        for _ in range(m - 1):
            prev = prev.next

        # Step 2: Reverse the sublist
        curr = prev.next
        for _ in range(n - m):
            temp = curr.next
            curr.next = temp.next
            temp.next = prev.next
            prev.next = temp

        # Step 3: Return the new head
        return dummy.next
