def get_values(digits):
    output = []
    if len(digits) == 1:
        output.append(digits)
    elif digits[0] == digits[-1] == "0":
        pass
    elif digits[0] == "0":
        output.append(digits[:1] + "." + digits[1:])
    elif digits[-1] == "0":
        output.append(digits)
    else:
        output.append(digits)
        for i in range(1, len(digits)):
            output.append(digits[:i] + "." + digits[i:])
    return output


class Solution:
    def ambiguousCoordinates(self, s: str) -> List[str]:
        digits = s[1:-1]
        output = set()
        for i in range (len(digits) - 1):
            prefixes = get_values(digits[:i + 1])
            sufixes = get_values(digits[i + 1:])
            for prefix in prefixes:
                for sufix in sufixes:
                    output.add("({}, {})".format(prefix, sufix))
        return output
