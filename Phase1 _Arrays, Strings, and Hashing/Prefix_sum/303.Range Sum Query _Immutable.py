class NumArray:
    def __init__(self, nums):
        
        self.nums = nums

    def sumRange(self, left, right):
        
        total = 0
        for i in range(left, right + 1):
            total += self.nums[i]
        return total

# The above is Brute force approach and results in time limit exceeded for large inputs on Leetcode


class NumArray:
    def __init__(self, nums):
        # build prefix sum array
        self.prefix = [0]
        for num in nums:
            self.prefix.append(self.prefix[-1] + num)

    def sumRange(self, left, right):
        # get range sum in O(1)
        return self.prefix[right + 1] - self.prefix[left]
    
    
# The above is Optimal approach using Prefix sum technique