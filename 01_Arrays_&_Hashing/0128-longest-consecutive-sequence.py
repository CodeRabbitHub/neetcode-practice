"""
Approach:
1. Use a Set for O(1) Lookups: Convert the list of numbers into a set to allow for O(1) average-time complexity checks.
2. Identify Sequence Start Points: Iterate through the set, and for each number, check if it is the start of a sequence 
(i.e., num - 1 is not in the set).
3. Count Consecutive Numbers: For each start point, count the length of the consecutive sequence by incrementing a 
counter until the next number in the sequence is not found in the set.
4. Track Maximum Length: Keep track of the maximum length of consecutive sequences encountered.

Time Complexity
O(n) - where n is the number of elements in the input list. Each number is processed at most twice
(once when checking if it's the start of a sequence, and once while counting the length of the sequence).

Space Complexity
O(n) - where n is the number of elements in the input list. This is due to storing elements in the set for O(1) lookups.

"""

from typing import List


class Solution:
    def longest_consecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        num_set = set(nums)
        max_length = 0

        for num in num_set:
            if num - 1 not in num_set:
                current_num = num
                current_length = 1

                while current_num + 1 in num_set:
                    current_num += 1
                    current_length += 1

                max_length = max(max_length, current_length)

        return max_length


# Example usage:
test = Solution()
print(test.longest_consecutive([100, 4, 200, 1, 3, 2]))  # Output: 4
print(test.longest_consecutive([0, 3, 7, 2, 5, 8, 4, 6, 0, 1]))  # Output: 9
