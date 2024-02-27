"""
Given an integer x, return true if x is a palindrome
, and false otherwise.
"""


class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """

        str_x = str(x)
        return str_x == str_x[::-1]


class Solution2(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False

        original = x
        reversed_num = 0
        while x > 0:
            reversed_num = reversed_num * 10 + x % 10
            x //= 10

        return original == reversed_num


test_cases = [
    (121, True),  # Basic palindrome
    (-121, False),  # Negative numbers are not palindromes
    (10, False),  # Edge case: numbers with trailing zeros
    (-101, False),  # Another negative number test
    (0, True),  # Single-digit '0' is a palindrome
    (12321, True),  # Longer palindrome
    (12345, False),  # Non-palindrome
]

for x, expected_output in test_cases:
    OUTPUT = Solution2().isPalindrome(x)
    assert (
        OUTPUT == expected_output
    ), f"Failed for input {x}, expected {expected_output}, got {OUTPUT}"

print("All test cases passed!")
