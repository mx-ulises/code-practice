class Solution:
    def winnerOfGame(self, colors: str) -> bool:
        if not colors:
            return False
        current_color = colors[0]
        current_color_count = 0
        multiplier = {"A": 1, "B": -1}
        count = 0
        for i in range(0, len(colors)):
            if current_color != colors[i]:
                count += multiplier[current_color] * max(current_color_count - 2, 0)
                current_color_count = 0
            current_color = colors[i]
            current_color_count += 1
        count += multiplier[current_color] * max(current_color_count - 2, 0)
        return (0 < count)
