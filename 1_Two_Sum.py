"""
Given an array of integers nums and an integer target, return indices of the two numbers 
such that they add up to target.

You may assume that each input would have exactly one solution, and 
you may not use the same element twice.

You can return the answer in any order.
"""


class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        for i, num in enumerate(nums):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]


# Test cases
test_cases = [
    ([2, 7, 11, 15], 9, [0, 1]),  # Basic case
    ([3, 2, 4], 6, [1, 2]),  # Elements not necessarily in order
    ([3, 3], 6, [0, 1]),  # Duplicate elements
    ([-1, 3, 7, 0], 0, [0, 3]),  # Negative numbers and zero
]

# Example of how to run the tests
for nums, target, expected_output in test_cases:
    solution = Solution()  # Create an instance of your Solution class
    result = solution.twoSum(nums, target)

    if result == expected_output:
        print(f"Test passed: Input: {nums}, Target: {target}, Output: {result}")
    else:
        print(
            f"Test failed! Input: {nums}, Target: {target}, Expected: {expected_output}, Got: {result}"
        )
