class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        # Compare every pair (i, j)
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                # Check if elements are equal and within distance k
                if nums[i] == nums[j] and abs(i - j) <= k:
                    return True
        return False

# 🔹 Example test
if __name__ == "__main__":
    sol = Solution()
    nums = [1, 2, 3, 1]
    k = 3
    print(sol.containsNearbyDuplicate(nums, k))  # Output: True

# The above is Brute force approach and results in time limit exceeded for large inputs on Leetcode

class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        window = set()
        
        for i in range(len(nums)):
            if nums[i] in window:
                return True
            window.add(nums[i])
            # Keep the window size at most k
            if len(window) > k:
                window.remove(nums[i - k])
        
        return False

# 🔹 Example test
if __name__ == "__main__":
    sol = Solution()
    nums = [1, 2, 3, 1]
    k = 3
    print(sol.containsNearbyDuplicate(nums, k))  # Output: True
    
# The above is Optimal approach using Sliding Window technique