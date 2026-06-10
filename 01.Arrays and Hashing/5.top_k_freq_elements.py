# Top K Frequent Elements - return the k most frequent elements within the array

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[] for i in range(len(nums) + 1)]

        for n in nums:
            count[n] = 1 + count.get(n, 0)
        for n, c in count.items():
            freq[c].append(n)
        res = []
        for i in range(len(freq) - 1, -1, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res
# Time Complexity: O(N) - We iterate through the nums array once to count the frequency of each element which takes O(N) time. Then through the frequency list, which takes O(N) time.
# Space Complexity: O(N) - We use a hash map to store the frequency of each element which takes O(N) space. The frequency list also takes O(N) space.
# - Use a hash map to count the frequency of each element in the nums array.
# - Create a list of lists (frequency list) where the index represents the frequency and the value at that index is a list of elements that have that frequency.
# - Iterate through the frequency list in reverse order and add elements to the result list until we have added k elements.

# Alternative Approach: Using a Min Heap to keep track of the top k elements. This approach has a time complexity of O(N log k) due to the heap operations.

# Another approach : Sorting the elements by frequency and then returning the top k elements. This approach has a time complexity of O(N log N) due to the sorting step.