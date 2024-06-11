"""
Determines if a given string is a valid palindrome, ignoring non-alphanumeric characters and case.

Approach:
1. Use two pointers to iterate over the input string from the beginning and end.
2. Ignore non-alphanumeric characters and compare the characters case-insensitively.
3. If all corresponding characters match, return True. Otherwise, return False.

Time Complexity:
O(n) - where n is the length of the input string. We iterate through the string once with two pointers.

Space Complexity:
O(1) - No extra space is used except for the pointers.

:param input_string: The input string to check for palindrome properties.
:return: True if the input string is a valid palindrome, False otherwise.
"""


class Solution:
    def valid_palindrome(self, input_string: str) -> bool:

        # Initialize two pointers
        left, right = 0, len(input_string) - 1

        while left < right:
            # Move the left pointer to the next alphanumeric character
            while left < right and not input_string[left].isalnum():
                left += 1
            # Move the right pointer to the previous alphanumeric character
            while left < right and not input_string[right].isalnum():
                right -= 1

            # Compare the characters case-insensitively
            if input_string[left].lower() != input_string[right].lower():
                return False

            left += 1
            right -= 1

        # If all characters matched, it's a palindrome
        return True


# Test the function
test = Solution()
print(test.valid_palindrome("A man, a plan, a canal: Panama"))  # Should return True
print(test.valid_palindrome("race a car"))  # Should return False
