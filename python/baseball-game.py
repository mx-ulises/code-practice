class Solution:
    def calPoints(self, operations: List[str]) -> int:
        records = []
        for operation in operations:
            if operation == "+":
                records.append(records[-1] + records[-2])
            elif operation == "D":
                records.append(records[-1] * 2)
            elif operation == "C":
                records.pop()
            else:
                records.append(int(operation))
        return sum(records)
