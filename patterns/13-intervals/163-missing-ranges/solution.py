from typing import List


class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[List[int]]:
        ranges = []
        prev = lower - 1

        for i in range(len(nums) + 1):
            curr = nums[i] if i < len(nums) else upper + 1

            if curr - prev > 1:
                ranges.append([prev + 1, curr - 1])

            prev = curr

        return ranges
