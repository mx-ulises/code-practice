OPERATIONS = {
    "+": 1,
    "-": -1,
}

class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        value = 0
        for operation in operations:
            value += OPERATIONS[operation[1]]
        return value
