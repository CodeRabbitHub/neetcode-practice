"""
Approach:
1. Create two arrays, left_products and right_products, where:
2. left_products[i] contains the product of all elements to the left of index i.
3. right_products[i] contains the product of all elements to the right of index i.
4. Compute the final result by multiplying corresponding elements of left_products and right_products.
5. Optimize the space complexity by using the result array directly instead of maintaining two separate arrays.

Time Complexity:
O(n) - We traverse the array three times: once to build left_products, once to build right_products, and once to compute the final result.

Space Complexity:
O(1) additional space (excluding the output array)
"""

from typing import List


class Solution:
    def product_except_self(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [1] * n

        # Step 1: Calculate left products and store in result
        left_product = 1
        for i in range(n):
            result[i] = left_product
            left_product *= nums[i]

        # Step 2: Calculate right products and multiply with corresponding left product
        right_product = 1
        for i in range(n - 1, -1, -1):
            result[i] *= right_product
            right_product *= nums[i]

        return result


# Test the implementation
test = Solution()
print(test.product_except_self([1, 2, 3, 4]))  # Output: [24, 12, 8, 6]
print(test.product_except_self([5, 6, 2, 3]))  # Output: [36, 30, 90, 60]
print(test.product_except_self([0, 0]))  # Output: [0, 0]
print(test.product_except_self([1, 0]))  # Output: [0, 1]
