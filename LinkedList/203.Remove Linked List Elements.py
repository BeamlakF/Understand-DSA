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
