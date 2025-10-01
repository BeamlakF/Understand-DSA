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