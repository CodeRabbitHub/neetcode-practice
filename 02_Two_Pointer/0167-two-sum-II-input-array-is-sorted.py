"""
Finds two indices such that the numbers at those indices in the sorted list add up to the target.

Approach:
1. Initialize two pointers, one at the beginning (left) and one at the end (right) of the list.
2. Iterate through the list while left < right:
    - If the sum of the numbers at indices left and right equals the target, return [left, right].
    - If the sum is less than the target, increment left to increase the sum.
    - If the sum is greater than the target, decrement right to decrease the sum.

Time Complexity:
O(n) - where n is the number of elements in the list. This is because we iterate through the list at most once with the two pointers.

Space Complexity:
O(1) - No extra space is used except for the indices.

:param numbers: The sorted list of numbers.
:param target: The target sum.
:return: A list containing the indices of the two numbers that add up to the target.
"""

from typing import List


class Solution:
    def two_sum_sorted(self, numbers: List[int], target: int) -> List[int]:

        left = 0
        right = len(numbers) - 1

        while left < right:
            current_sum = numbers[left] + numbers[right]
            if current_sum == target:
                return [left, right]
            elif current_sum < target:
                left += 1
            else:
                right -= 1

        # If no solution is found
        return []


# Test the function
test = Solution()
print(test.two_sum_sorted([2, 7, 11, 15], 9))  # Should return [0, 1]
print(test.two_sum_sorted([1, 2, 3, 4, 4, 9], 8))  # Should return [3, 4]
print(test.two_sum_sorted([1, 3, 5, 7, 9], 12))  # Should return [2, 4]
print(test.two_sum_sorted([1, 2, 3, 4, 5], 10))  # Should return []
