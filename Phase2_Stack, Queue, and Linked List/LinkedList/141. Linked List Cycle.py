class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        seen = set() #set is a built-in type in python that does not allow duplicates
        curr = head
        
        while curr:
            if curr in seen:
                return True
            else:
                seen.add(curr)
            curr = curr.next
            
           
        return False
    
# Time Complexity: O(n)
# Space Complexity: O(n)
        