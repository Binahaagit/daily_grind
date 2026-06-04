# Given an array of integers nums and an integer target, return the indices i and j such that nums[i] + nums[j] == target and i != j

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        pHash = {}

        for i, n in enumerate(nums):
            diff = target - n
            if diff in pHash:
                return [pHash[diff], i]
            pHash[n] = i
        return
        
# Time Complexity: O(N) - We iterate through the list once.
# Space Complexity: O(N) - In the worst case, the hash map stores N elements.
# - Use a Hash Map to store previously seen numbers and their indices for O(1) average-time lookups.
# - For each number, calculate the difference needed to reach the target and check if it exists in the hash map.
# - Early Exit: Return the indices as soon as a valid pair is found.


# Alternative Approach: Brute Force
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return
# Time Complexity: O(N^2) - We check every pair of numbers.
# Space Complexity: O(1) - We use only a constant amount of extra space.
