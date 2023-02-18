def get_longest_balanced_substring(s: str) -> int:
    stack = []
    maximal_len = 0
    last_helthy = -1
    for i in range(len(s)):
        if s[i] == '(':
            stack.append(i)
        elif len(stack) == 0:
            last_helthy = i
        else:
            stack.pop()
            j = last_helthy
            if len(stack):
                j = stack[-1]
            maximal_len = max(maximal_len, i - j)
    return maximal_len


def test(s, expected):
    value = get_longest_balanced_substring(s)
    print (f"value: {value}, expected: {expected}, string: '{s}'")
    assert(value == expected)


TEST_CASES = [
    ("(())(", 4),
    ("(())()", 6),
    (")))(((", 0),
    (")))()(((", 2),
    ("(((()", 2),
    ("()()()", 6),
    ("))())(())((())(())((", 8),
]

for (s, expected) in TEST_CASES:
    test(s, expected)
