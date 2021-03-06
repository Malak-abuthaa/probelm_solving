"""Implement
the
Stack


class in your favorite programming language (should have two separate implementations)


Array
implementation
Linked
list
implementation
[execution time limit]
4
seconds(py3)"""


#########################################

# import requests
# import mysql.connector
# import pandas as pd

class stack_arr:
    def __init__(self):
        self.stack = []
        self.index = -1

    def push(self, value):
        self.index += 1
        self.stack.append(value)

    def pop(self):
        self.index -= 1

    def size(self):
        return self.index + 1

    def top(self):
        return self.stack[self.index] if self.index != -1 else None


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class stack_LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def push(self, value):
        if self.head == None:
            self.head = Node(value)
        else:
            newn_node = Node(value)
            newn_node = self.head
            self.head = newn_node
        size += 1

    def pop(self):
        if self.head == None:
            return None
        else:
            popped_node = self.head
            self.head = self.head.next
            self.size -= 1
            return popped_node

    def size(self):
        return self.size

    def top(self):
        return self.head.value if self.head else None



