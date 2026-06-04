# Question: Contains Duplicate


class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        s = set()
        
        for n in nums:
            if n in s:
                return True   
            s.add(n)
        return False



# Time Complexity: O(N) - We iterate through the list exactly once.
# Space Complexity: O(N) - In the worst case, the set stores N elements.

# - Use a Hash Set to store visited elements for O(1) average-time lookups.
# - Early Exit: Return True the moment a duplicate is hit.