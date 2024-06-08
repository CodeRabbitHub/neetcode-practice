"""
Determines if a list contains any duplicates.

Approach:
1. Create an empty set to keep track of seen numbers.
2. Iterate through each number in the list.
3. If the number is already in the set, return True (duplicate found).
4. If the number is not in the set, add it to the set.
5. If no duplicates are found after checking all numbers, return False.

Time Complexity:
O(n) - where n is the number of elements in the list. This is because we iterate through the list once.

Space Complexity:
O(n) - In the worst case, we may store all n elements in the set if there are no duplicates.
"""

from typing import List


class Solution:
    def contains_duplicate(self, nums: List[int]) -> bool:
        seen = set()
        for num in nums:
            if num in seen:
                return True
            else:
                seen.add(num)
        return False


test = Solution()
print(test.contains_duplicate(nums=[1, 2, 3, 1]))
print(test.contains_duplicate(nums=[1, 2, 3, 4]))
print(test.contains_duplicate(nums=[1, 1, 1, 3, 3, 4, 3, 2, 4, 2]))
