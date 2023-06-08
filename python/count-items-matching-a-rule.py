KEY_MAP = {
    "type": 0,
    "color": 1,
    "name": 2,
}

class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        index = KEY_MAP[ruleKey]
        matches = 0
        for item in items:
            if item[index] == ruleValue:
                matches += 1
        return matches
