""""Given a Matrix of ones and zeros, write a function (solution) that returns the size of the largest contiguous block of zeros.

For example, for the input:

matrix = [
   [0, 0, 0, 0, 1, 1, 1],
   [0, 0, 0, 0, 1, 1, 0],
   [0, 1, 1, 1, 1, 1, 1],
   [1, 1, 1, 0, 0, 1, 1],
   [1, 1, 1, 1, 0, 1, 1],
]
The largest contiguous block is the one in the top left corner, which contains 9 zeros (solution = 9)

Tip: two elements are not within the same blocks if they are only connected diagonally.

[execution time limit] 4 seconds (py3)

[input] array.array.integer matrix

The input matrix is an array of arrays, where the values are either 1 or 0.

[output] integer

The size of the largest contiguous block of zeros"""


def solution(grid):
    def dfs(r, c):

        # base case:

        if not (0 <= r < h) or not (0 <= c < w):
            # Stop due to being out of boundary
            return 0

        if grid[r][c] != 0:
            # Stop due to being out of current island
            return 0

            # general cases:

            # mark current grid to -1 as visited
        grid[r][c] = -1

        # update area of current island
        return 1 + dfs(r - 1, c) + dfs(r + 1, c) + dfs(r, c - 1) + dfs(r, c + 1)

        # -------------------------------

    h, w = len(grid), len(grid[0])

    max_island_area = 0

    # Search all possible islands in DFS
    for r in range(h):
        for c in range(w):

            if grid[r][c] == 0:
                cur_island_area = dfs(r, c)

                max_island_area = max(max_island_area, cur_island_area)

    return max_island_area


