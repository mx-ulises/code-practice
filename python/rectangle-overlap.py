class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        if rec1[2] <= rec2[0] or rec2[2] <= rec1[0]:
            return False
        if rec2[2] <= rec1[0] or rec1[2] <= rec2[0]:
            return False
        if rec1[3] <= rec2[1] or rec2[3] <= rec1[1]:
            return False
        if rec2[3] <= rec1[1] or rec1[3] <= rec2[1]:
            return False
        return True
