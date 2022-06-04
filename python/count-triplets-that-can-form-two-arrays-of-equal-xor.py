class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        triplet_count = 0
        n = len(arr)
        cumulative_arr = [0]
        for i in range(n):
            cumulative_arr.append(cumulative_arr[-1] ^ arr[i])
        for i in range(n):
            for k in range(i + 1, n):
                c = cumulative_arr[i] ^ cumulative_arr[k + 1]
                if c == 0:
                    triplet_count += k - i
        return triplet_count
