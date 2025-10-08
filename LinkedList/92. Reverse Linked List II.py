class Solution:
    def reverseBetween(self, head: Optional[ListNode], m: int, n: int) -> Optional[ListNode]:
        # Step 0: dummy node to simplify edge cases
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy

        # step 1: move prev to the node just before position m
        for _ in range(m-1):
            prev = prev.next
        # Now prev is at (m-1)th node

        # Step 2: reverse the sublist from m to n
        curr = prev.next
        tail = curr
        for _ in range(n-m):
            next_temp = curr.next
            curr.next = next_temp.next
            next_temp.next =prev.next
            prev.next = next_temp

     
        # Step 3: reconnect reversed sublist with prev and the remaining list
        tail.next = curr.next
        curr.next = next_temp

        # Step 4: return new head
        return dummy.next
