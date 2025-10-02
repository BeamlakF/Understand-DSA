class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # Step 1: collect values into a Python list
        values = []
        curr = head
        while curr:
            values.append(curr.val)
            curr = curr.next

        # Step 2: check if values equal reversed(values)
        return values == values[::-1]
##Space Complexity: O(n)

        ### Approach 2 : Reverse the second half and compare

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return True

        # Step 1: find the middle (slow/fast trick)
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Step 2: reverse the second half (starting at slow)
        prev = None
        curr = slow
        while curr:
            next_temp = curr.next
            curr.next = prev
            prev = curr
            curr = next_temp
        # Now prev is the head of the reversed second half

        # Step 3: compare first half and reversed second half
        left, right = head, prev
        while right:  # only need to check second half
            if left.val != right.val:   ### TODO 1: mismatch → return False
                return False
            left = left.next            ### TODO 2: move left forward
            right = right.next          ### TODO 3: move right forward

        return True
