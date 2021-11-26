"""Implement
the
Queue


class in your favorite programming language (should have two separate implementations):


Array
implementation
Linked
list
implementation
[execution time limit]
4
seconds(py3)
"""


######################################################

# import requests
# import mysql.connector
# import pandas as pd
class queue_arr:

    def __init__(self, capacity):
        self.buffer = [0] * capacity
        self.size = 0
        self.capacity = capacity
        self.head_index = 0
        self.tail_index = 0

    def push_element(self, value):
        if self.size == self.capacity:
            raise Exception('The circular buffer is full.')
        self.buffer[self.tail_index] = value
        self.tail_index = (self.tail_index + 1) % self.capacity
        self.size += 1

    def pop_element(self):
        if self.size == 0:
            raise Exception('Popping from an empty circular buffer.')
        ret = self.buffer[self.head_index]
        self.head_index = (self.head_index + 1) % self.capacity
        self.size -= 1
        return ret

    def peek_head(self):
        if self.size == 0:
            raise Exception('Peeking into an empty circular buffer.')
        return self.buffer[self.head_index]

    def increase_capacity(self, new_cap):
        temp = [] * new_cap
        for i in (self.head_index, self.tail_index + 1):
            temp.append(self.buffer[i])
        self.capacity = new_cap
        self.buffer = temp
        self.tail_index = self.tail_index - self.head_index
        self.head_index = 0


class Node:

    def __init__(self, value):
        self.value = value
        self.next = None


class queue_node:

    def __init__(self):
        self.front = self.last = None
        self.size = 0

    def push(self, value):
        temp = Node(value)
        if (self.front == None):
            self.front = self.last = temp

        self.last.next = temp
        self.last = temp
        self.size += 1

    def pop(self):
        if (self.front == None):
            return None
        temp = self.front
        self.front = self.front.next

        if self.front == None:
            self.last = None
        self.size -= 1

        return temp.value

    def size(self):

        return self.size

