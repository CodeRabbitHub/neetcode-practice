"""
Approach:
1. Create a frequency dictionary to count the occurrences of each element.
2. Use a heap to keep track of the top K elements.
3. Iterate through the frequency dictionary, adding elements to the heap.
4. If the heap size exceeds K, remove the smallest element.
5. Extract the elements from the heap, which will be the top K frequent elements.

Time Complexity:
O(n log k) - where n is the number of elements in the list and k is the number of top frequent elements. Building the frequency dictionary takes O(n), and maintaining the heap takes O(log k) time for each of the n elements.

Space Complexity:
O(n) - In the worst case, we store all n elements in the frequency dictionary.

"""

from typing import List
import heapq
from collections import Counter


class Solution:
    def top_k_frequent(self, nums: List[int], k: int) -> List[int]:
        frequency_dict = Counter(nums)
        heap = []
        for num, freq in frequency_dict.items():
            heapq.heappush(heap, (freq, num))
            if len(heap) > k:
                heapq.heappop(heap)
        top_k_elements = [num for freq, num in heap]
        return top_k_elements


test = Solution()
print(test.top_k_frequent([1, 1, 1, 2, 2, 3], 2))
print(test.top_k_frequent([1], 1))
print(test.top_k_frequent([4, 1, -1, 2, -1, 2, 3], 2))
