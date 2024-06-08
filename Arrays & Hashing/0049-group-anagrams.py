"""
Approach:
1. Create an empty dictionary to store groups of anagrams.
2. Iterate through each word in the list.
3. Sort the word to get a common representation for anagrams.
4. Use the sorted word as a key in the dictionary.
5. If the key exists, append the original word to the list of anagrams.
6. If the key does not exist, create a new list with the original word.
7. Return the values of the dictionary, which are the grouped anagrams.

Time Complexity:
O(n * k log k) - where n is the number of words in the list and k is the maximum length of a word. Sorting each word takes O(k log k) time.

Space Complexity:
O(n * k) - In the worst case, we store all n words in the dictionary with each word having up to k characters.
"""

from typing import List


class Solution:
    def group_anagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams_map = {}

        for word in strs:
            sorted_word = "".join(sorted(word))
            if sorted_word in anagrams_map:
                anagrams_map[sorted_word].append(word)
            else:
                anagrams_map[sorted_word] = [word]

        return list(anagrams_map.values())


# Test the implementation
test = Solution()
print(test.group_anagrams(strs=["eat", "tea", "tan", "ate", "nat", "bat"]))
print(test.group_anagrams(strs=[""]))
print(test.group_anagrams(strs=["a"]))
