"""Implement Heap Sort using your preferred programming language

[execution time limit] 4 seconds (py3)"""


class Heap:

    def __init__(self):
        self.arr = []

    def heapfiy(self):
        if len(self.arr) == 0:
            return "heap is empty"

        t = self.arr[-1]
        self.arr.pop()
        return t

    def put(self, v):
        if len(self.arr) == 0:
            self.arr.append(v)
            return
        if v <= self.arr[-1]:
            self.arr.append(v)
            return
        elif v >= self.arr[0]:
            self.arr.insert(0, v)
            return

        for i in range(1, len(self.arr) - 1):
            if v <= self.arr[i]:
                self.arr.insert(i + 1, v)

    def printHeap(self):
        print(self.arr)


