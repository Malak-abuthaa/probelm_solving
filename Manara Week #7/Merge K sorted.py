# import requests
# import mysql.connector
# import pandas as pd

# Definition for singly-linked list.

"""
https://leetcode.com/problems/merge-k-sorted-lists/
Time = O(n^2)
space  = O(N)"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


import heapq


class Solution:
    def mergeKLists(self, lists):
        pq = []

        for i in range(len(lists)):
            temp = lists[i]
            while temp:
                heapq.heappush(pq, temp.val)
                temp = temp.next

        res = ListNode(0)
        header = res
        while pq:
            header.next = ListNode(heappop(pq))
            header = header.next

        return res.next

