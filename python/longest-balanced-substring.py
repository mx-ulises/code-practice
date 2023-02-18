def get_longest_balanced_substring(s: str) -> int:
    stack = []
    maximal_len = 0
    current_streak = 0
    for i in range(len(s)):
        c = s[i]
        current_streak += 1
        if c == '(':
            stack.append((c, i))
        elif len(stack) == 0:
            current_streak = 0
        else:
            _, j = stack.pop()
            maximal_len = max(maximal_len, i - j + 1)
            if len(stack) == 0:
                maximal_len = max(maximal_len, current_streak)
    return maximal_len


def test(s, expected):
    value = get_longest_balanced_substring(s)
    print (f"value: {value}, expected: {expected}")
    assert(get_longest_balanced_substring(s) == expected)


TEST_CASES = [
    ("(())(", 4),
    ("(())()", 6),
    (")))(((", 0),
    (")))()(((", 2),
    ("(((()", 2),
    ("()()()", 6),
]

for (s, expected) in TEST_CASES:
    test(s, expected)
