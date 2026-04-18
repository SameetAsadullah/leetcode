from typing import List


class Solution:
    """
    Problem Idea:
    Use a hash map to remember numbers we have already seen and their indices.

    Algorithm:
    1. Iterate through the array once.
    2. For each number, compute its complement: target - number.
    3. If the complement is already in the hash map, return both indices.
    4. Otherwise, store the current number and its index in the hash map.

    Why It Works:
    When we reach a number whose complement has already appeared, the hash map
    gives us the earlier index immediately, so we find the pair in one pass.

    Time Complexity: O(n)
    Space Complexity: O(n)
    """

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}  # number -> index

        for index, num in enumerate(nums):
            complement = target - num
            if complement in seen:
                return [seen[complement], index]
            seen[num] = index

        return []
