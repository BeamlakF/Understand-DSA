class Solution:
    def deleteNode(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        # Step 1: copy all values into a Python list
        values = []
        curr = head
        while curr:
            values.append(curr)
            curr = curr.next

        if val in values:
            values.remove(val)

    


        # Step 3: rebuild linked list from values
        dummy = ListNode(0)
        curr = dummy
        for v in values:
            new_node = ListNode(v)
            curr.next = new_node
            curr = curr.next
            
            pass

        # Step 4: return the new head
        return dummy.next
