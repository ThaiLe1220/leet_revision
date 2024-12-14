"""
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Constraints:

1 <= strs.length <= 200
0 <= strs[i].length <= 200
strs[i] consists of only lowercase English letters.

"""


class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""

        prefix = strs[0]

        for string in strs[1:]:
            while string.find(prefix) != 0:
                prefix = prefix[:-1]

        return prefix


# Test cases
test_cases = [
    (["flower", "flow", "flight"], "fl"),
    (["flow", "flow", "flow"], "flow"),
    (["flower", "flower", "flow"], "flow"),
    (["dog", "racecar", "car", "care"], ""),
]

for idx, (test_case, expected_output) in enumerate(test_cases):
    solution = Solution()
    result = solution.longestCommonPrefix(test_case)

    if result == expected_output:
        print(f"Test Case {idx + 1}: Test Passed")
    else:
        print(f"Test Case {idx + 1}: Test Failed")
    print()

# # Example of how to run the tests
# for nums, target, expected_output in test_cases:
#     solution = Solution()  # Create an instance of your Solution class
#     result = solution.twoSum(nums, target)

#     if result == expected_output:
#         print(f"Test passed: Input: {nums}, Target: {target}, Output: {result}")
#     else:
#         print(
#             f"Test failed! Input: {nums}, Target: {target}, Expected: {expected_output}, Got: {result}"
#         )
