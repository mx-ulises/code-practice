class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        deck.sort()
        positions = deque([i for i in range(len(deck))])
        output = [0] * len(deck)
        while positions:
            output[positions.popleft()] = deck.pop(0)
            if positions:
                index = positions.popleft()
                positions.append(index)
        return output
