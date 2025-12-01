class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        count = 0
        prefix = 0
        freq = {0: -1}
        

        for i in range(0, len(nums)):
            if nums[i] == 1:
                prefix = prefix + 1
            else:
                prefix = prefix - 1 
            
            if prefix in freq:
                length = i - freq[prefix]
                count = max( count, length)
            
            else:
                freq[prefix] = i

        return count
                
    
        