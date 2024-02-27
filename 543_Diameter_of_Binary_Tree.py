"""
Given the root of a binary tree, return the length of the diameter of the tree.

The diameter of a binary tree is the length of the longest path between any 
two nodes in a tree. This path may or may not pass through the root.

The length of a path between two nodes is represented by the number of edges between them.
"""

import unittest  # Import the unittest module


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.longest_diameter = 0

        def calculate_height(node):
            if not node:
                return 0

            left_height = calculate_height(node.left)
            right_height = calculate_height(node.right)

            self.longest_diameter = max(
                self.longest_diameter, left_height + right_height
            )

            return 1 + max(left_height, right_height)

        calculate_height(root)
        return self.longest_diameter


class TestDiameterOfBinaryTree(unittest.TestCase):
    def test_simple_tree(self):
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        solution = Solution()
        self.assertEqual(solution.diameterOfBinaryTree(root), 2)

    def test_skewed_tree(self):
        root = TreeNode(1)
        root.right = TreeNode(2)
        root.right.right = TreeNode(3)
        solution = Solution()
        self.assertEqual(solution.diameterOfBinaryTree(root), 2)

    def test_larger_tree(self):
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        root.left.left = TreeNode(4)
        root.left.right = TreeNode(5)
        solution = Solution()
        self.assertEqual(solution.diameterOfBinaryTree(root), 3)


if __name__ == "__main__":
    unittest.main()
