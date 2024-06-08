"""
Approach:
1. If the lengths of the two strings are not the same, they cannot be anagrams.
2. Create dictionaries to count the frequency of each character in both strings.
3. Compare the two dictionaries. If they are identical, the strings are anagrams; otherwise, they are not.

Time Complexity:
O(n) - where n is the length of the strings. This is because we iterate over both strings once to create the
frequency dictionaries and then perform a comparison of the dictionaries.

Space Complexity:
O(1) - In the worst case, the space required is proportional to the number of unique characters in the strings.
Since there are only a fixed number of characters (e.g., 26 lowercase English letters), this space is constant.
"""


class Solution:
    def is_anagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        char_count_s = {}
        char_count_t = {}

        for char in s:
            char_count_s[char] = char_count_s.get(char, 0) + 1

        for char in t:
            char_count_t[char] = char_count_t.get(char, 0) + 1

        return char_count_s == char_count_t


test = Solution()

print(test.is_anagram(s="anagram", t="nagaram"))
print(test.is_anagram(s="rat", t="car"))
