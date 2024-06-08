"""
Finds two indices such that the numbers at those indices in the list add up to the target.

Approach:
1. Initialize an empty dictionary to store the complement of each number and its index.
2. Iterate through the list of numbers using an index and value.
3. For each number, check if it exists in the dictionary (i.e., if its complement was seen before).
4. If it exists, return the stored index of the complement and the current index.
5. If it doesn't exist, compute its complement with respect to the target and store the complement and index in the dictionary.

Time Complexity:
O(n) - where n is the number of elements in the list. This is because we iterate through the list once.

Space Complexity:
O(n) - In the worst case, we may store all n elements in the dictionary if no solution is found until the end.
"""

from typing import List


class Solution:
    def two_sum(self, nums: List[int], target: int) -> List[int]:
        compliment_dict = {}
        for idx, num in enumerate(nums):
            if num in compliment_dict:
                return [compliment_dict[num], idx]
            else:
                compliment = target - num
                compliment_dict[compliment] = idx


test = Solution()
print(test.two_sum(nums=[2, 7, 11, 15], target=9))
print(test.two_sum(nums=[3, 2, 4], target=6))
print(test.two_sum(nums=[3, 3], target=6))
