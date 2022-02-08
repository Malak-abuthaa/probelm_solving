""""
here are N network nodes, labeled from 1 to N.

Given times, a list of travel times as directed edges times[i] = (u, v, w), where u is the source node, v is the target node, and w is the time it takes for a signal to travel from source to target.

Now, we send a signal from a certain node K. How long will it take for all nodes to receive the signal? If it is impossible, return -1.

Example:

Input: times = [[2,1,1],[2,3,1],[3,4,1]], N = 4, K = 2
Output: 2
"""
import heapq as heap


def solution(times, n, k):
    graph = {}
    dist = {}
    q = []

    for u, v, w in times:
        if u not in graph:
            graph[u] = []

        graph[u].append((v, w))

    heap.heappush(q, (0, k))

    while q:
        d, node = heap.heappop(q)
        if node in dist:
            continue
        dist[node] = d
        if node in graph:
            for v, newdist in graph[node]:
                if v not in dist:
                    heap.heappush(q, (d + newdist, v))

    if len(dist) == n:
        return max(dist.values())
    return -1


