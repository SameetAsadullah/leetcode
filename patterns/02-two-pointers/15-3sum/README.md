# 3Sum

- LeetCode Problem #: 15
- Pattern: Two Pointers
- Link: https://leetcode.com/problems/3sum/

## Problem

Given an integer array `nums`, return all the triplets
`[nums[i], nums[j], nums[k]]` such that:

- `i != j`
- `i != k`
- `j != k`
- `nums[i] + nums[j] + nums[k] == 0`

The solution set must not contain duplicate triplets.

## Example

```text
Input: nums = [-1, 0, 1, 2, -1, -4]
Output: [[-1, -1, 2], [-1, 0, 1]]
```

## Constraints

- `3 <= nums.length <= 3000`
- `-10^5 <= nums[i] <= 10^5`

## Algorithm

Sort the array, then fix one number and solve the remaining part with two
pointers.

1. Sort `nums`.
2. Loop through the array with index `i` as the first number of the triplet.
3. Skip duplicate values for `i` to avoid duplicate triplets.
4. Use `left = i + 1` and `right = len(nums) - 1`.
5. If the sum is too small, move `left` rightward.
6. If the sum is too large, move `right` leftward.
7. If the sum is zero, record the triplet and skip duplicate values for
   `left` and `right`.

## Why It Works

After sorting, moving `left` to the right increases the sum, and moving
`right` to the left decreases it. That makes the inner search efficient.

Skipping duplicates at `i`, `left`, and `right` ensures each valid triplet is
added only once.

## Complexity

- Time: `O(n^2)`
- Space: `O(1)` extra space, excluding the output and Python's sort internals

## Solution

```python
from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []

        for i in range(len(nums)):
            if nums[i] > 0:
                break

            if i > 0 and nums[i] == nums[i - 1]:
                continue

            left = i + 1
            right = len(nums) - 1

            while left < right:
                total = nums[i] + nums[left] + nums[right]

                if total < 0:
                    left += 1
                elif total > 0:
                    right -= 1
                else:
                    result.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1

                    while left < right and nums[left] == nums[left - 1]:
                        left += 1

                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1

        return result
```
