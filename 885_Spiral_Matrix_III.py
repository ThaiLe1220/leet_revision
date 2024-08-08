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
        position = [rStart, cStart]
        print(f"Start + {position}")

        # Define directions:
        directions = [
            # (x, y)
            (1, 0),  # East
            (0, -1),  # South
            (-1, 0),  # West
            (0, 1),  # North
        ]
        steps = [1, 1, 2, 2]

        def walk(position, direction):
            position[0] += direction[0]
            position[1] += direction[1]

            return position

        while len(result) < rows * cols:
            for direction, step in zip(directions, steps):
                for _ in range(step):
                    position = walk(position, direction)
                    print(position)
                    if -1 < position[0] < cols and -1 < position[1] < rows:
                        result.append(position[:])  # Append a copy of the position

            steps = [s + 2 for s in steps]

        return result


# Test cases
def run_test_case(rows, cols, rStart, cStart):
    sol = Solution()
    print(f"Input: rows = {rows}, cols = {cols}, rStart = {rStart}, cStart = {cStart}")
    result = sol.spiralMatrixIII(rows, cols, rStart, cStart)

    print(f"Output: {result}")
    print()


# Easy test case
# run_test_case(1, 4, 0, 0)
run_test_case(1, 4, 3, 0)

# # Medium test case
# print("Medium Test Case:")
# run_test_case(5, 6, 1, 4)

# # Hard test case
# print("Hard Test Case:")
# run_test_case(50, 50, 25, 25)
