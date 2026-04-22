from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}
        buckets = [[] for _ in range(len(nums) + 1)]
        result = []

        for num in nums:
            counts[num] = counts.get(num, 0) + 1

        for num, frequency in counts.items():
            buckets[frequency].append(num)

        for frequency in range(len(buckets) - 1, 0, -1):
            for num in buckets[frequency]:
                result.append(num)
                if len(result) == k:
                    return result

        return result
