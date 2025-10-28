class NumArray:
    def __init__(self, nums):
        
        self.nums = nums

    def sumRange(self, left, right):
        
        total = 0
        for i in range(left, right + 1):
            total += self.nums[i]
        return total

# The above is Brute force approach and results in time limit exceeded for large inputs on Leetcode