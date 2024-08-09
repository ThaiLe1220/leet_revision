"""
A 3 x 3 magic square is a 3 x 3 grid filled with distinct numbers from 1 to 9 such that each row, column, and both
diagonals all have the sum 

Given a row x col grid of integers, how many 3 x 3 contiguous magic square subgrids are there?

Note: while a magic square can only contain numbers from 1 to 9, grid may contain numbers up to 15.
"""


class Solution(object):
    def numMagicSquaresInside(self, grid):
        count = 0
        rows = len(grid)
        cols = len(grid[0])
        print()
        print(rows, "x", cols, end="\n\n")

        # may be first check if how many 3x3 can be fit into grid
        # numbers of 3x3 grid = (rows - 3) * (cols - 3)
        # in the meantime also check for valid 3x3
        # start with only accepting number from 1 to 9
        # then we check for diagonals rules of sum
        # return the magic square count
        if rows < 3 or cols < 3:
            return 0
        else:
            # find 3x3 edge
            for r in range(2, rows):
                for c in range(2, cols):
                    print(r - 2, "x", c - 2, end=" | ")
                    print(r, "x", c, end=" | ")
                    print(r - 1, "x", c - 1, end=" | ")
                    print("{", grid[r - 1][c - 1], "}")

                    if grid[r - 1][c - 1] != 5:
                        break

                    diagonal_1 = grid[r - 2][c - 2] + grid[r][c] + 5
                    diagonal_2 = grid[r - 2][c] + grid[r][c - 2] + 5

                    row_1 = grid[r - 2][c - 2] + grid[r - 2][c - 1] + grid[r - 2][c]
                    row_2 = grid[r - 1][c - 2] + 5 + grid[r - 1][c]

                    col_1 = grid[r - 2][c - 2] + grid[r - 1][c - 2] + grid[r][c - 2]
                    col_2 = grid[r][c - 1] + 5 + grid[r - 2][c - 1]

                    if (
                        diagonal_1
                        == diagonal_2
                        == row_1
                        == row_2
                        == 15
                        == col_1
                        == col_2
                        and 0 < grid[r - 2][c - 2] < 10
                        and 0 < grid[r - 1][c - 2] < 10
                        and 0 < grid[r - 2][c - 1] < 10
                    ):
                        print(grid[r - 2][c - 2], "+", grid[r][c], end=" | ")
                        print(grid[r - 2][c], "+", grid[r][c - 2])
                        count += 1

            return count


# Test cases
def test_solution():
    solution = Solution()

    # Easy test case
    grid1 = [[4, 3, 8, 4], [9, 5, 1, 9], [2, 7, 6, 2]]

    assert solution.numMagicSquaresInside(grid1) == 1

    # Medium test case
    grid2 = [[5, 5, 5], [5, 5, 5], [5, 5, 5]]
    assert solution.numMagicSquaresInside(grid2) == 0

    # # Hard test case
    # grid3 = [
    #     [2, 7, 6, 9, 5, 1, 4, 3, 8],
    #     [6, 1, 8, 7, 5, 3, 2, 9, 4],
    #     [7, 5, 3, 2, 9, 4, 8, 6, 1],
    #     [6, 4, 5, 1, 8, 9, 3, 2, 7],
    #     [5, 9, 1, 7, 3, 2, 6, 4, 8],
    #     [3, 8, 2, 4, 6, 5, 1, 7, 9],
    #     [9, 3, 4, 6, 2, 7, 5, 8, 1],
    #     [1, 6, 7, 5, 4, 8, 9, 3, 2],
    #     [8, 2, 9, 3, 1, 6, 7, 5, 4],
    # ]
    # assert solution.numMagicSquaresInside(grid3) == 9

    # print("All tests passed!")


test_solution()
