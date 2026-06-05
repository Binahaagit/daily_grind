# Given an array of strings strs, group all anagrams together into sublists.
# Input: strs = ["act","pots","tops","cat","stop","hat"]
# Output: [["hat"],["act", "cat"],["stop", "pots", "tops"]]

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        map = defaultdict(list)

        for word in strs:
            count = [0]*26
            for char in word:
                count[ord(char)-ord('a')] += 1
            map[tuple(count)].append(word)
        return list(map.values())
        
# Time Complexity: O(N*K) - We iterate through each of the N strings and for each string, we count the frequency of characters which takes O(K) time.
# Space Complexity: O(N*K) - In the worst case, all strings are different and we store all of them in the hash map. The count array takes O(1) space since it has a fixed size of 26 for lowercase letters.
# - Use a hash map to group anagrams together. The key is a tuple representing the frequency of each character in the string.
# - For each string, create a count array of size 26 to count the frequency of each character (assuming only lowercase letters).
# - Convert the count array to a tuple and use it as a key in the hash map.



# Alternative Approach: Sorting
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        map = defaultdict(list)

        for word in strs:
            sorted_word = ''.join(sorted(word))
            map[sorted_word].append(word)
        return list(map.values())
# Time Complexity: O(N*K log K) - We iterate through each of the N strings and for each string, we sort it which takes O(K log K) time.
# Space Complexity: O(N*K) - In the worst case, all strings are different and we store all of them in the hash map. Sorting creates new strings which also take O(K) space.