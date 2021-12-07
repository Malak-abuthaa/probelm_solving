"""

Python Binary Search Tree: Find the closest value of a target in a given non-empty Binary Search Tree (BST) of unique values
"""
# class TreeNode:
#     def __init__(self, val):
#         self.val = val
#         self.right = None
#         self.left = None
#
# def find_closest(tree, target, colsest= - float('inf')):
#     if root is None:
#         return colsest
#     if root.val - target > closest:
#         closest = root.val - target
#     elif root.val > target:
#         return find_closest(root.left, target, closest)
#     elif root.val < target:
#         return find_closest(root.right, target, closest)
#
# if __name__ == '__main__':
#
#     tree = TreeNode(1)
#     tree.right = 2
#     tree.left = 5
#     print(tree, 10)


class TreeNode(object):

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def closest_value(root, target):
    a = root.val
    kid = root.left if target < a else root.right
    if not kid:
        return a
    b = closest_value(kid, target)
    return min((a, b), key=lambda x: abs(target - x))


root = TreeNode(8)
root.left = TreeNode(5)
root.right = TreeNode(14)
root.left.left = TreeNode(4)
root.left.right = TreeNode(6)
root.left.right.left = TreeNode(8)
root.left.right.right = TreeNode(7)
root.right.right = TreeNode(24)
root.right.right.left = TreeNode(22)

result = closest_value(root, 19)
print(result)
