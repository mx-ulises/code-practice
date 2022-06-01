class Solution:
    def interpret(self, command: str) -> str:
        output = []
        current_string = 0
        for c in command:
            if c == "G":
                output.append("G")
            elif c == ")" and current_string == 1:
                output.append("o")
                current_string = 0
            elif c == ")" and current_string == 3:
                output.append("al")
                current_string = 0
            else:
                current_string += 1
        return "".join(output)
