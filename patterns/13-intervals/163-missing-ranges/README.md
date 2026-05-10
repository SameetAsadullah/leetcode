# Missing Ranges

- LeetCode Problem #: 163
- Pattern: Intervals
- Link: https://leetcode.com/problems/missing-ranges/

## Problem

You are given an inclusive range `[lower, upper]` and a sorted unique integer
array `nums`, where all elements are within the inclusive range.

Return the shortest sorted list of ranges that exactly covers all the missing
numbers in `[lower, upper]`.

## Example

```text
Input: nums = [0,1,3,50,75], lower = 0, upper = 99
Output: [[2,2],[4,49],[51,74],[76,99]]
```

## Constraints

- `-10^9 <= lower <= upper <= 10^9`
- `0 <= nums.length <= 100`
- `lower <= nums[i] <= upper`
- All values in `nums` are unique
- `nums` is sorted in ascending order

## Algorithm

Scan the array and look at the gap between consecutive values.

1. Pretend there is a value just before the range, `lower - 1`.
2. Traverse `nums`, and after the loop pretend there is a value just after the
   range, `upper + 1`.
3. For each pair `prev` and `curr`, if `curr - prev > 1`, then the missing
   range is `[prev + 1, curr - 1]`.
4. Add that range to the answer.

## Why It Works

Every missing range must lie between two known boundary values:
- either between two consecutive numbers in `nums`
- or between a bound and the nearest number in `nums`

By using `lower - 1` and `upper + 1` as artificial boundaries, the same gap
logic handles the beginning, middle, and end of the range uniformly.

## Complexity

**Time:** `O(n)`

We make one pass through the array, plus one extra iteration to handle the
final boundary at `upper + 1`. Each step does only constant-time arithmetic and
comparison, so the runtime grows linearly with `nums.length`.

**Space:** `O(1)` extra space, excluding the output

Aside from `prev`, `curr`, and the loop index, no auxiliary data structure is
used. The returned list of missing ranges is the required output, so it is not
counted as extra space here.

## Solution

```python
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
```
