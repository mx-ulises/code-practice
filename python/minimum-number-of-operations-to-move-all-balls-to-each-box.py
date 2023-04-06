class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        left_count, left_moves = 0, 0
        right_count, right_moves = 0, 0
        operations = []
        for i in range(1, len(boxes)):
            if boxes[i] == '1':
                right_count += 1
                right_moves += i
        operations.append(left_moves + right_moves)
        for i in range(1, len(boxes)):
            if boxes[i - 1] == '1':
                left_count += 1
            left_moves += left_count
            right_moves -= right_count
            if boxes[i] == '1':
                right_count -= 1
            operations.append(left_moves + right_moves)
        return operations
