""""
Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.

[execution time limit] 4 seconds (py3)

Time = O(N+M )
space O(N+M)
"""
class Node:
    def __init__(self, next=None, prev=None, data=None):
        self.next = next
        self.data = data
        self.prev = prev


class LinkedList:
    def __init__(self):
        self.head = None  # Initally there are no elements in the list
        self.tail = None

    def insert(self, value):
        if head is None:
            self.head = Node(self.tail, None, value)
        else:
            self.tail = Node(None, self.head, value)

    def find(self, target):
        temp = self.head
        while temp != None:
            if temp.data == target:
                return True
            temp = temp.next
        return False

    def delete(self):
        temp = self.head
        while temp != None:
            if temp.data == target:
                temp.prev = temp.next
            temp = temp.next

    def value(self):
        return self.tail.data


def merge_two_list(nodeA, nodeB):
    if nodeA is None:
        return nodeB
    if nodeB is None:
        return nodeA

    res = LinkedList()

    while nodeA and nodeB:
        if nodeA.data <= nodeB.data:
            res.insert(nodeA.data)
            nodeA = nodeA.next
        else:
            res.insert(nodeB)
            nodeB = nodeB.next
    if nodeA is not None:
        while nodeA:
            res.insert(nodeA)
            nodeA = nodeA.next

    elif nodeB is not None:
        while nodeB:
            res.insert(nodeB)
            nodeB = nodeB.next
    return res


