

"""
Implement a doubly linked list with the following 4 operations:

Insert at head,
insert at tail,
find and
delete

"""
# import requests
# import mysql.connector
# import pandas as pd


# Node of a doubly linked list
class Node:
    def __init__(self, next=None, prev=None, data=None):
        self.next = next
        self.prev = prev
        self.data = data


class DoublyLinkedList:
    def __init__(self):
        self.head = None  # Initally there are no elements in the list
        self.tail = None

    def insert_to_head(self, value):

        self.head = Node(self.head, None, value)

    def insert_to_tail(self, value):

        self.tail = Node(None, self.tail, value)

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

