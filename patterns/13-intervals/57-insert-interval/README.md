# Insert Interval

- LeetCode Problem #: 57
- Pattern: Intervals
- Link: https://leetcode.com/problems/insert-interval/

## Problem

You are given an array of non-overlapping intervals `intervals` where
`intervals[i] = [start_i, end_i]` represent the start and the end of the `i`th
interval, and `intervals` is sorted in ascending order by `start_i`.

Insert `newInterval` into `intervals` such that `intervals` is still sorted in
ascending order by `start_i` and `intervals` still does not have any
overlapping intervals after merging if necessary.

Return `intervals` after the insertion.

## Example

```text
Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
Output: [[1,5],[6,9]]
```

## Constraints

- `0 <= intervals.length <= 10^4`
- `intervals[i].length == 2`
- `0 <= start_i <= end_i <= 10^5`
- `intervals` is sorted by `start_i` in ascending order
- `intervals` has no overlapping intervals
- `newInterval.length == 2`
- `0 <= newInterval[0] <= newInterval[1] <= 10^5`

## Algorithm

Process the array in three parts:

1. Add all intervals that end before `newInterval` starts.
2. Merge all intervals that overlap with `newInterval`.
3. Add the merged interval, then append the remaining intervals.

## Why It Works

Because the input intervals are already sorted and non-overlapping:

- all intervals completely before `newInterval` can be copied directly
- all overlapping intervals appear in one continuous block
- all remaining intervals come after the merged interval

That lets us solve the problem in one pass.

## Complexity

**Time:** `O(n)`

The algorithm walks through the input in three phases, but the index `i` only
moves forward and never resets. That means every interval is examined at most
once: either copied before the merge, absorbed into `newInterval`, or appended
afterward. So the total work remains linear.

**Space:** `O(n)` for the output

The returned list can contain nearly all original intervals, plus the merged
interval that replaces the overlapping block. Since we build a new result list,
the output size is the main space cost.

## Solution

```python
from typing import List


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        result = []
        i = 0

        while i < len(intervals) and intervals[i][1] < newInterval[0]:
            result.append(intervals[i])
            i += 1

        while i < len(intervals) and intervals[i][0] <= newInterval[1]:
            newInterval[0] = min(newInterval[0], intervals[i][0])
            newInterval[1] = max(newInterval[1], intervals[i][1])
            i += 1

        result.append(newInterval)
        result.extend(intervals[i:])

        return result
```
