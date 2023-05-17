class Solution:
    def non_optimal(n: int, k: int) -> int:
        if k == 1:
            return n
        graph = [i + 1 for i in range(n + 1)]
        graph[n] = 1
        current_friend = 0
        while graph[current_friend] != current_friend:
            for i in range(k - 1):
                current_friend = graph[current_friend]
            next_friend = graph[current_friend]
            graph[current_friend] = graph[next_friend]
        return current_friend

    def optimal(n: int, k: int) -> int:
        pos = 0
        for i in range(2, n + 1):
            pos = ((pos + k) % i)
        return pos + 1

    def findTheWinner(self, n: int, k: int) -> int:
        return Solution.optimal(n, k)
