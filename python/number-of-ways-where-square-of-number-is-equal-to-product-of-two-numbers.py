def get_count(nums):
    count_num = defaultdict(lambda: 0)
    for num in nums:
        count_num[num] += 1
    return count_num


def get_triplet_count(count_num, nums):
    triplet_count = 0
    for a in count_num:
        a2 = a * a
        aux_count = defaultdict(lambda: 0)
        for b in nums:
            if (a2) % b == 0:
                c = int(a2 / b)
                triplet_count += count_num[a] * aux_count[c]
            aux_count[b] += 1
    return triplet_count


class Solution:

    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        triplet_count = 0
        count_num_1 = get_count(nums1)
        count_num_2 = get_count(nums2)
        triplet_count += get_triplet_count(count_num_1, nums2)
        triplet_count += get_triplet_count(count_num_2, nums1)
        return triplet_count
