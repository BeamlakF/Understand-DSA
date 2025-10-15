class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        
        while head and head.val == val:
            head = head.next
            
        curr = head
        while curr and curr.next:
            if curr.next.val == val:
                curr.next = curr.next.next
                ### That’s how one “unlink” a node in a linked list.
            else:
                curr = curr.next
                ### if nothing is removed, then move curr forward

        # Step 3: return the (possibly updated) head
        return head


        ### Approach 2 : Brute force

class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        # Step 1: put all values into a list
        values = []
        curr = head
        while curr:
            values.append(curr.val)
            curr = curr.next

        # Step 2: filter out the unwanted values
        filtered = []
        for v in values:
            if v != val:
                filtered.append(v)

        # Step 3: rebuild linked list from filtered values
        dummy = ListNode(0)
        curr = dummy
        for v in filtered:
            curr.next = ListNode(v)
            curr = curr.next

        # Step 4: return the new head
        return dummy.next
