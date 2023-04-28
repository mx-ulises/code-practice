class Solution:
    def stack_solution(nums: List[int]) -> List[int]:
        positives = []
        negatives = []
        answer = []
        while nums:
            num = nums.pop()
            if num < 0:
                negatives.append(num)
            if 0 < num:
                positives.append(num)
        while negatives and positives:
            answer.append(positives.pop())
            answer.append(negatives.pop())
        return answer


    def array_solution(nums: List[int]) -> List[int]:
        answer = [0] * len(nums)
        positive_i, negative_i = 0, 1
        for num in nums:
            if 0 < num:
                answer[positive_i] = num
                positive_i += 2
            else:
                answer[negative_i] = num
                negative_i += 2
        return answer


    def rearrangeArray(self, nums: List[int]) -> List[int]:
        return Solution.stack_solution(nums)
