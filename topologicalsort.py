####
#   Requires an adjacency matrix given by adjacencymatrixbuilder.py, returns a topological sort of all the nodes
####

stack = []
aocMatrix = {75: [29, 53, 47, 61], 47: [61, 53, 29], 61: [29, 53], 53: [29]}
adjacencyMatrix = {
    1: [2, 3, 4],
    2: [5, 6],
    3: [7],
    4: [7, 8],
    6: [9, 10],
    7: [11],
    10: [11],
}


def topologicalSort(node: int, listOfAdjacentNodes: list) -> None:
    if (not listOfAdjacentNodes) and (node not in stack):
        stack.insert(0, node)

    for eachNode in listOfAdjacentNodes.copy():
        topologicalSort(
            node=eachNode,
            listOfAdjacentNodes=adjacencyMatrix.get(eachNode, []),
        )
        listOfAdjacentNodes.remove(eachNode)

    if node not in stack:
        stack.insert(0, node)


if __name__ == "__main__":
    topologicalSort(75, aocMatrix[75])
    print(stack)
