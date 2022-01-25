def solution_heap(nums, k):
    maximals = []
    dequeued = []
    window = []
    for i in range(k):
        heappush(window, -nums[i])
    for j in range(k, len(nums)):
        maximals.append(-window[0])
        i = j - k
        heappush(dequeued, -nums[i])
        while dequeued and dequeued[0] == window[0]:
            heappop(window)
            heappop(dequeued)
        heappush(window, -nums[j])
    maximals.append(-window[0])
    return maximals


def solution_dequeue(nums, k):
    maximals = []
    window = deque()
    for i in range(k):
        while window and window[-1] < nums[i]:
            window.pop()
        window.append(nums[i])
    maximals.append(window[0])
    for j in range(k, len(nums)):
        if window[0] == nums[j - k]:
            window.popleft()
        while window and window[-1] < nums[j]:
            window.pop()
        window.append(nums[j])
        maximals.append(window[0])
    return maximals


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        #return solution_heap(nums, k)
        return solution_dequeue(nums, k)
