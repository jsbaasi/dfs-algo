####
#   Requires an adjacency matrix given by adjacencymatrixbuilder.py, returns a DFS walk of all the nodes
####

stack = []
# {75: [29, 53, 47, 61], 47: [61, 53, 29], 61: [29, 53], 53: [29]}
adjacencyMatrix = {
    1: [2, 3, 4],
    2: [5, 6],
    3: [7],
    4: [7, 8],
    6: [9, 10],
    7: [11],
    10: [11],
}


def dfs(node: int, listOfAdjacentNodes: list) -> None:
    if node not in stack:
        stack.append(node)
    if not listOfAdjacentNodes:
        return
    for node in listOfAdjacentNodes:
        dfs(
            node=node,
            listOfAdjacentNodes=adjacencyMatrix.get(node, []),
        )


if __name__ == "__main__":
    dfs(1, adjacencyMatrix[1])
    print(stack)
