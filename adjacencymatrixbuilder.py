####
# Advent of code Day 5 rules are formatted as "x|y"
####
testAOCSet: set = {
    "61|53",
    "47|29",
    "75|29",
    "75|47",
    "47|61",
    "47|53",
    "75|61",
    "75|53",
    "61|29",
    "53|29",
}


def adventOfCodeAdjacencyMatrix(ruleSet: set[str]) -> dict[int, list]:
    adjacencyMatrix: dict[int, list] = {}
    for rule in ruleSet:
        firstNumber, secondNumber = rule.split("|")
        adjacencyMatrix.setdefault(int(firstNumber), []).append(int(secondNumber))
    return adjacencyMatrix


print(adventOfCodeAdjacencyMatrix(testAOCSet))

# testAOCAdjMatrix = {75: [29, 53, 47, 61], 47: [61, 53, 29], 61: [29, 53], 53: [29]}
