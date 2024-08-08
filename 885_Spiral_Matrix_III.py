"""
  N
W   E
  S

You start at the cell (rStart, cStart) of an rows x cols grid facing east. The northwest corner 
is at the first row and column in the grid, and the southeast corner is at the last row and column.

You will walk in a clockwise spiral shape to visit every position in this grid. Whenever you move 
outside the grid's boundary, we continue or walk outside the grid (but may return to the boundary 
later). Eventually we reach all rows * cols spaces of the grid.

Return an array of coordinates representing the positions of the grid in the order you visit them.
"""


class Solution(object):
    def spiralMatrixIII(self, rows, cols, rStart, cStart):
        # Initialize result list with the starting position
        result = [[rStart, cStart]]

        # Define directions:
        directions = [
            # (x, y)
            (1, 0),  # East
            (0, 1),  # South
            (-1, 0),  # West
            (0, -1),  # North
        ]

        # Initialize variables for the spiral walk
        steps = 0
        direction = 0
        position = [rStart, cStart]

        def walk(position, direction):
            position[0] += direction[0]
            position[1] += direction[1]

            return position

        while len(result) < rows * cols:
            # move in spiral
            position = walk(position, directions[0])
            # if new_position in grid -> add to result

            # continue until fill out results
            pass

        print(result[0])
        print(walk(result[0], directions[0]))

        return result


# Test cases
def run_test_case(rows, cols, rStart, cStart):
    sol = Solution()
    print(f"Input: rows = {rows}, cols = {cols}, rStart = {rStart}, cStart = {cStart}")
    result = sol.spiralMatrixIII(rows, cols, rStart, cStart)

    # print(f"Output: {result}")
    # print(f"Number of positions visited: {len(result)}")
    # print("Expected number of positions:", rows * cols)
    print()


# Easy test case
run_test_case(1, 4, 0, 0)
run_test_case(1, 4, 0, 3)

# # Medium test case
# print("Medium Test Case:")
# run_test_case(5, 6, 1, 4)

# # Hard test case
# print("Hard Test Case:")
# run_test_case(50, 50, 25, 25)
