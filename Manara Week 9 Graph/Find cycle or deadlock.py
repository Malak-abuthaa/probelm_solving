"""In a multithreaded environment, it's possible that different processes will need to use the same resource. A wait-for graph represents the different processes as nodes in a directed graph, where an edge from node i to node j means that the node j is using a resource that node i needs to use (and cannot use until node j releases it).

We are interested in whether or not this digraph has any cycles in it. If it does, it is possible for the system to get into a state where no process can complete.

We will represent the processes by integers 0, ...., n - 1. We represent the edges using a two-dimensional list connections. If j is in the list connections[i], then there is a directed edge from process i to process j.

Write a function that returns True if connections describes a graph with a directed cycle, or False otherwise.

Example

For connections = [[1], [2], [3, 4], [4], [0]], the output should be
solution(connections) = true.


This graph contains a cycle.

For connections = [[1, 2, 3], [2, 3], [3], []], the output should be
solution(connections) = false.


This graph doesn't contain a directed cycle (there are two paths from 0 to 3, but no paths from 3 back to 0).

Input/Output

[execution time limit] 4 seconds (py3)

[input] array.array.integer connections

A representation of the graphs edges. connection.length is the number of vertices. If j is in the list connections[i], then there is a directed edge from process i to process j.

Guaranteed constraints:
1 ≤ connections.length ≤ 500,
0 ≤ connections[i][j] < connections.length,
connections[i][j] ≠ connections[i][k] for j ≠ k,
i not in connections[i].

[output] boolean

Return True if connections describes a graph with a directed cycle, or False otherwise."""


# two solution for this either uing stack to backtracking or dict
def solution(connections):
    # use fact that a cyclic graph must be bipartite
    v = [0] * len(connections)

    # all nodes with v 0 are not visited
    def DFS(node):
        if v[node] == 0:
            v[node] = 1  # once node is visited v is made 1
            for nei in connections[node]:
                if v[nei] == 1:
                    # if node with v 1 has a neighbor with v 1, then cycle
                    return True
                if DFS(nei):  # recursively run through the neighbors with DFS and see if exists cycle
                    return True
            v[node] = 2
        # base case of a sink node will start with v = 2 then it will

    # recursively run backwards and keep changing all to 2s if no cycle
    # is found in the neigboring nodes that are not v 2

    for i in range(len(connections)):
        check = DFS(i)
        if check:
            return True
    return False

