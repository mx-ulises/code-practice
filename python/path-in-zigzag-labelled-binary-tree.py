class Solution:
    def get_tree_level(label: int) -> int:
        level = 0
        while 0 < label:
            level += 1
            label //= 2
        return level

    def get_inversed(value: int, level: int) -> int:
        level_min = 2 ** (level - 1)
        level_max = level_min * 2 - 1
        position = (level_max - value) + level_min
        return position

    def get_label_or_position(value: int, level: int) -> int:
        if level % 2 == 0:
            value = Solution.get_inversed(value, level)
        return value

    def pathInZigZagTree(self, label: int) -> List[int]:
        level = Solution.get_tree_level(label)
        path = []
        while 0 < level:
            path.append(label)
            parent_position = Solution.get_label_or_position(label, level) // 2
            level -= 1
            label = Solution.get_label_or_position(parent_position, level)
        path.reverse()
        return path
