"""
Encodes a list of strings to a single string.

Approach:
1. Use a delimiter that is unlikely to appear in the strings (e.g., a combination of special characters).
2. Join the list of strings using the delimiter.

Time Complexity: O(n) where n is the total number of characters in all strings combined.
Space Complexity: O(1) for additional space used, excluding the input and output.

Decodes a single string to a list of strings.

Approach:
1. Split the encoded string using the same delimiter used during encoding.

Time Complexity: O(n) where n is the total number of characters in the encoded string.
Space Complexity: O(1) for additional space used, excluding the input and output.
"""

from typing import List


class Codec:
    def encode(self, strs: List[str]) -> str:

        delimiter = chr(257)  # Using a non-ASCII character as a delimiter.
        return delimiter.join(strs)

    def decode(self, s: str) -> List[str]:

        delimiter = chr(257)  # The same delimiter used in encoding.
        return s.split(delimiter)


# Example usage:
codec = Codec()
original_list = ["Hello", "World", "Encode", "Decode"]
encoded_string = codec.encode(original_list)
decoded_list = codec.decode(encoded_string)

print(f"Original list: {original_list}")
print(f"Encoded string: {encoded_string}")
print(f"Decoded list: {decoded_list}")
