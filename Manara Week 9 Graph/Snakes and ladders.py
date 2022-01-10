"""You probably played Snakes and Ladders when you were a kid. Since it's been a while, let's review the rules:

Each player puts their counter on the start position.
Roll the dice. Move your counter forward the number of spaces shown on the dice.
If your counter lands at the bottom of a ladder, you must move up to the top of the ladder.
If your counter lands on the head of a snake, you must slide down to the bottom of the snake.
The first player to get to the finish position is the winner.
We will use a standard six-sided dice.

You are given the length of the gameboard boardSize, a list of all the snakes, where snakes[i] = [a, b] means the snake with its head on position a and its tail on position b, and a list of all the ladders, where ladders[i] = [a, b] means the ladder with its bottom on position a and its top on position b. Return the length of the shortest possible path between the start (cell 1) and finish (cell boardSize) positions of the game.

Example

For boardSize = 30, snakes = [[27, 1], [21, 9], [17, 4], [19, 7]], and ladders = [[11, 26], [3, 22], [5, 8], [20, 29]], the output should be
solution(boardSize, snakes, ladders) = 3.



One of the possible shortest paths between cell 1 and cell 30 is set by the following dice throws: [4, 3, 4]. Indeed, the first dice throw 4 leads us to cell 5, which has a ladder to cell 8. So, after the first throw we stand on cell 8. Then, the second throw 3 leads us to cell 11 and the ladder there leads us to cell 26. After this, the last dice throw 4 leads us to the final position.

Input/Output

[execution time limit] 4 seconds (py3)

[input] integer boardSize

The number of cells in the game board.

Guaranteed constraints:
1 ≤ boardSize ≤ 105.

[input] array.array.integer snakes

The list of all the snakes on the board, where snakes[i] = [a, b] means the snake with its head on position a and its tail on position b.

Guaranteed constraints:
0 ≤ snakes.length ≤ 104,
snakes[i].length = 2,
1 ≤ snakes[i][0], snakes[i][1] ≤ boardSize - 1,
snakes[i][0] > snakes[i][1]."""

from collections import deque


def solution(n, snakes, ladders):
    temp = {}

    for i in range(len(snakes)):
        temp[snakes[i][0]] = snakes[i][1]
    snakes = temp
    temp = {}
    for i in range(len(ladders)):
        if ladders[i][0] not in snakes and ladders[i][1] not in snakes:
            temp[ladders[i][0]] = ladders[i][1]
    ladders = temp
    edges = []
    for i in range(n):

        j = 1
        while j <= 6 and i + j <= n:
            src = i

            # update destination if there is any ladder
            # or snake from the current position.

            _ladder = ladders.get(i + j) if (ladders.get(i + j)) else 0
            _snake = snakes.get(i + j) if (snakes.get(i + j)) else 0

            if _ladder or _snake:
                dest = _ladder + _snake
            else:
                dest = i + j

            # add an edge from src to dest
            edges.append((src, dest))

            j = j + 1

    # construct a directed graph
    g = Graph(edges, n)

    # Find the shortest path between 1 and 100 using BFS
    return BFS(g, 0, n)


class Graph:
    # Constructor
    def __init__(self, edges, n):
        # A list of lists to represent an adjacency list
        self.adjList = [[] for _ in range(n)]

        # add edges to the graph
        for (src, dest) in edges:
            # Please note that the graph is directed
            self.adjList[src].append(dest)


# Perform BFS on graph `g` starting from a given source vertex
def BFS(g, source, n):
    # create a queue for doing BFS
    q = deque()

    # to keep track of whether a vertex is discovered or not
    discovered = [False] * (n + 1)

    # mark the source vertex as discovered
    discovered[source] = True

    # assign the minimum distance of the source vertex as 0 and
    # enqueue it
    q.append((source, 0))

    # loop till queue is empty
    while q:

        # dequeue front node
        vertex, min_dist = q.popleft()

        # `vertex` stores the number associated with the graph node
        # `min_dist` stores the minimum distance of a node from the starting vertex

        # Stop BFS if the last node is reached
        if vertex == n:
            return min_dist

        # do for every adjacent node of the current node
        for u in g.adjList[vertex]:
            if not discovered[u]:
                # mark it as discovered and enqueue it
                discovered[u] = True

                # assign the minimum distance of the current node
                # one more than the minimum distance of the parent node
                q.append((u, min_dist + 1))