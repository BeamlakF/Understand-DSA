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

# Time Complexity: O(n)
# Space Complexity: O(n)


# Approach 2: In-Place Deletion
class Solution:
    def deleteNode(self, node: ListNode) -> None:
        """
        Deletes the given node (except the tail) in a singly linked list.
        NOT given the head of the list.
        """
        node.val = node.next.val
        # TODO 1: Copy the value from the next node into the current node
        

        node.next = node.next.next
        pass 
        # TODO 2: Skip over the next node
        


       
