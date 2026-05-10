# Non-overlapping Intervals

- LeetCode Problem #: 435
- Pattern: Intervals
- Link: https://leetcode.com/problems/non-overlapping-intervals/

## Problem

Given an array of intervals `intervals` where `intervals[i] = [start_i, end_i]`,
return the minimum number of intervals you need to remove to make the rest of
the intervals non-overlapping.

## Example

```text
Input: intervals = [[1,2],[2,3],[3,4],[1,3]]
Output: 1
```

## Constraints

- `1 <= intervals.length <= 10^5`
- `intervals[i].length == 2`
- `-5 * 10^4 <= start_i < end_i <= 5 * 10^4`

## Algorithm

Sort the intervals by end time, then greedily keep the interval that finishes
first.

1. Sort by interval end.
2. Keep track of the end of the last interval we decided to keep.
3. For each next interval:
4. If it starts before the previous kept end, it overlaps, so remove it.
5. Otherwise, keep it and update the previous end.

## Why It Works

When two intervals overlap, keeping the one that ends earlier is always the
better greedy choice because it leaves more room for future intervals.

By sorting by end time first, every time we decide to keep an interval, we are
choosing the one that gives the best chance of fitting the maximum number of
non-overlapping intervals afterward. Minimizing removals is the same as
maximizing how many intervals we keep.

## Complexity

**Time:** `O(n log n)`

Sorting the intervals by end time costs `O(n log n)`. After that, we make one
linear pass through the sorted list and compare each interval once with the
last interval we kept. The sorting step dominates the final complexity.

**Space:** `O(1)` extra space, excluding Python's sort internals

The greedy scan only uses the removal counter and the previous end value. No
additional data structure is built during the pass.

## Solution

```python
from typing import List


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda interval: interval[1])
        removals = 0
        prev_end = intervals[0][1]

        for start, end in intervals[1:]:
            if start < prev_end:
                removals += 1
            else:
                prev_end = end

        return removals
```
