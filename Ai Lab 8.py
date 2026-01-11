values = {
    "1": 1, "18": 18, "10": 10, "9": 9, "7": 7, "11": 11,
    "6": 6, "13": 13, "12": 12, "19": 19, "0": 0, "15": 15, "4": 4
}

tree = {
    "A": ["B", "C", "D"],
    "B": ["E", "F"],
    "C": ["0", "15"],
    "D": ["G", "4"],
    "E": ["1", "H"],
    "F": ["9", "I"],
    "G": ["J", "K"],
    "H": ["18", "10"],
    "I": ["7", "11"],
    "J": ["6", "13"],
    "K": ["12", "19"]
}

def minimax(node, is_max):
    if node in values:
        return values[node]

    children = tree[node]

    if is_max:
        best = float('-inf')
        for child in children:
            best = max(best, minimax(child, False))
        return best
    else:
        best = float('inf')
        for child in children:
            best = min(best, minimax(child, True))
        return best

result_task1 = minimax("A", True)
print("MAX value at root A =", result_task1)