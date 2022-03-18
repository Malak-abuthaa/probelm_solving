"""Write a function that takes a list of file names and prints a directory tree structure from the files.

Feedback :
Ask the niterviewr if it possible to user sort or not
The diff between sort and sorted, sort is in place
How to save graph in dictronery
"""


def find_all_paths(arr):
    graph={}
    for item in arr:
        paths = item.split('/')
        pivot = graph
        print(paths)

        for path in paths:
            # this if statment solved the issue
            if path not in pivot:
                pivot[path] = {}
            pivot = pivot[path]
        print("after loop", graph)

    def dfs(pivot, spaces):
        if pivot is not None:
            for child in sorted(pivot.keys()):
                print( " "*spaces, "-",child)
                dfs(pivot[child], spaces + 1)

    dfs(graph,1)

print(find_all_paths([
	'foo/b/c',
	'bar/g',
	'foo/e',
	'foo/b/d',
	'bar/k',
	'bar/h/i/j'
]))