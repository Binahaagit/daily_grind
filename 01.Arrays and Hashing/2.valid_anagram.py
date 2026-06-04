# To check if 2 strings are anagrams. (They have the same characters but in a different order)

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        countS, countT = {}, {}

        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)
        
        for c in countS:
            if countS[c] != countT.get(c, 0):
                return False
        
        return True

# Time Complexity: O(N) - We iterate through both strings once.
# Space Complexity: O(1) - The count dictionaries will at most store 26 characters (assuming only lowercase letters).
# - Use two hash maps to count the frequency of each character in both strings.
# - Compare the frequency counts to determine if the strings are anagrams.
# - Early Exit: If the lengths of the strings differ, return False immediately.
# - The get method of dictionaries is used to handle missing keys gracefully, returning 0 for characters not present in the other string.

# Alternative Approach: Sorting
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)
# Time Complexity: O(N log N) - Sorting both strings takes O(N log N).
# Space Complexity: O(N) - Sorting creates new lists for the sorted characters.

# another alternative approach: using a single hash map
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        count = {}

        for i in range(len(s)):
            count[s[i]] = 1 + count.get(s[i], 0)
            count[t[i]] = count.get(t[i], 0) - 1
        
        for c in count:
            if count[c] != 0:
                return False
        
        return True
# Time Complexity: O(N) - We iterate through both strings once.
# Space Complexity: O(1) - The count dictionary will at most store 26 characters    