"""
Given a positive integer n, find the pivot integer x such that:
- The sum of all elements between 1 and x inclusively equals the sum of all elements 
between x and n inclusively.

Return the pivot integer x. If no such integer exists, return -1. It is guarantee that
there will be at mose one pivot index for the given input
"""


class Solution_Me(object):
    def pivotInteger(self, n):
        def sum(start, end):
            return (start + end) * (end - start + 1) // 2

        sum_all = sum(1, n)

        if n == 1:
            return 1

        for i in range(1, n):
            cur_sum = sum(1, i)
            left_sum = sum_all - cur_sum + i
            # print(f"[{i}]", cur_sum, ",", left_sum)

            if cur_sum == left_sum:
                # print(f"[{i}]", cur_sum, ",", left_sum)
                return i

        return -1


class Solution(object):
    def pivotInteger(self, n):
        # Calculate the total sum from 1 to n
        total_sum = n * (n + 1) // 2
        print()
        print(total_sum)

        # Calculate the square root of the total sum
        pivot = int((total_sum) ** 0.5)
        # print(total_sum**0.5)

        # Check if the pivot is valid
        if pivot * pivot == total_sum:
            return pivot

        return -1


sol = Solution()
sol.pivotInteger(1)
sol.pivotInteger(8)
sol.pivotInteger(49)
sol.pivotInteger(288)

# for i in range(10000):
#     res = sol.pivotInteger(i)
#     if res != -1:
#         print(i)
