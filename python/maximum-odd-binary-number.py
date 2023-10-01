class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        dq = deque()
        for c in s:
            if c == '0':
                dq.append('0')
            else:
                dq.appendleft('1')
        dq.append(dq.popleft())
        return "".join(dq)
