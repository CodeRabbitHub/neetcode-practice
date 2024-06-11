"""
Finds the maximum amount of water a container can hold using an array of heights, where each height
represents a vertical line drawn at that index.

Approach:
1. Use two pointers to iterate over the array from the beginning and end.
2. Calculate the area formed by the lines at these two pointers.
3. Move the pointer pointing to the shorter line inward to potentially find a larger area.
4. Repeat until the two pointers meet.
5. Return the maximum area found.

Time Complexity:
O(n) - where n is the length of the input array. We iterate through the array once with two pointers.

Space Complexity:
O(1) - No extra space is used except for the pointers.

:param height: List[int] - A list of non-negative integers representing the heights of vertical lines.
:return: int - The maximum area of water that can be contained.
"""


class Solution:
    def max_area(self, height: list[int]) -> int:
        # Initialize two pointers
        left, right = 0, len(height) - 1
        max_area = 0

        while left < right:
            # Calculate the width and the minimum height
            width = right - left
            min_height = min(height[left], height[right])

            # Calculate the current area
            current_area = width * min_height

            # Update the maximum area if current area is larger
            max_area = max(max_area, current_area)

            # Move the pointer pointing to the shorter line inward
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        # Return the maximum area found
        return max_area


# Test the function
test = Solution()
print(test.max_area([1, 8, 6, 2, 5, 4, 8, 3, 7]))  # Should return 49
print(test.max_area([1, 1]))  # Should return 1
