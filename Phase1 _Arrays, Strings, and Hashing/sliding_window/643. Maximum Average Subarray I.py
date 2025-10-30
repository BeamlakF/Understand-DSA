class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        max_sum = float('-inf')

        # Loop through all subarrays of length k
        for i in range(len(nums) - k + 1):
            current_sum = 0
            # Sum the elements in the window
            for j in range(i, i + k):
                current_sum += nums[j]
            max_sum = max(max_sum, current_sum)

        # Return the maximum average
        return max_sum / k

# 🔹 Example test
if __name__ == "__main__":
    sol = Solution()
    nums = [1, 12, -5, -6, 50, 3]
    k = 4
    print(sol.findMaxAverage(nums, k))  # Output: 12.75

# The above is Brute force approach and results in time limit exceeded for large inputs on Leetcode


class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        max_sum = float('-inf')

        # Loop through all subarrays of length k
        for i in range(len(nums) - k + 1):
            current_sum = 0
            # Sum the elements in the window
            for j in range(i, i + k):
                current_sum += nums[j]
            max_sum = max(max_sum, current_sum)

        # Return the maximum average
        return max_sum / k

# 🔹 Example test
if __name__ == "__main__":
    sol = Solution()
    nums = [1, 12, -5, -6, 50, 3]
    k = 4
    print(sol.findMaxAverage(nums, k))  # Output: 12.75
