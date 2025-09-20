class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        count = 0
        curr = head
        while curr:
            count = count +1
            curr = curr.next
        middle_index = count // 2

        curr = head
        for _ in range(middle_index):
            curr = curr.next
            

        return curr
