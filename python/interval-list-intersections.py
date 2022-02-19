def getOverlap(first, second):
    a = max(first[0], second[0])
    b = min(first[1], second[1])
    if a <= b:
        return (a, b)
    return None


class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        output = []
        while firstList and secondList:
            overlap = getOverlap(firstList[0], secondList[0])
            if overlap:
                output.append(overlap)
            if firstList[0][1] < secondList[0][1]:
                firstList.pop(0)
            else:
                secondList.pop(0)
        return output
