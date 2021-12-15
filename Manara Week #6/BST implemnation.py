""""

Time =  O(n log n )
Space = O(1)

    def insert(self, val):


Time =  O(n log n + n  )
Space = O(1)

    def delete(self, root, val):

Time =  O(n log n   )
Space = O(1)

    def search(self, val ):





mplement a Binary Search algorithm using your preferred programming language
"""


# import requests
# import mysql.connector
# import pandas as pd


class BinaryTree:

    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    def insert(self, val):
        if self.val is None:
            self.val = val
        else:
            if val == self.val:
                return "no duplicate alllowed in BST"
            if val < self.val:
                if self.left:
                    self.left.insert(val)
                else:
                    self.left = BinaryTree(val)
            elif val > self.val:
                if self.right:
                    self.right.insert(val)
                else:
                    self.right = BinaryTree(val)

    def delete(self, root, val):

        if not root:
            return root
        if root.val > val:
            root.left = delete(root.left, val)
        elif root.val < val:
            root.right = delete(root.right, val)
        else:

            if not root.right:
                return root.left

            if not root.left:
                return root.right
            temp_val = root.right
            mini_val = temp_val.val
            while temp_val.left:
                temp_val = temp_val.left
                mini_val = temp_val.val
            root.right = delete(root.right, root.val)
        return root

    def search(self, val):
        if self.val == val:
            return True
        if sefl.val is None:
            return False

        if val > self.val:
            self.right.search(val)
        else:
            self.left.search(val)








