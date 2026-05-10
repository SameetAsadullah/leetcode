# Merge Intervals

- LeetCode Problem #: 56
- Pattern: Intervals
- Link: https://leetcode.com/problems/merge-intervals/

## Problem

Given an array of intervals where `intervals[i] = [start_i, end_i]`, merge all
overlapping intervals and return an array of the non-overlapping intervals that
cover all the intervals in the input.

## Example

```text
Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
```

## Constraints

- `1 <= intervals.length <= 10^4`
- `intervals[i].length == 2`
- `0 <= start_i <= end_i <= 10^4`

## Algorithm

Sort the intervals by starting point, then scan from left to right while
merging overlaps.

1. Sort intervals by their start value.
2. Put the first interval into the result list.
3. For each next interval:
4. If it overlaps with the last merged interval, extend the end.
5. Otherwise, start a new merged interval.

## Why It Works

After sorting, any possible overlap for the current interval can only happen
with the last interval already placed in the merged result.

If the current interval starts before or at the end of the last merged
interval, they overlap and should be combined. Otherwise, they are disjoint and
should stay separate.

## Complexity

- Time: `O(n log n)` because of sorting
- Space: `O(n)` for the output

## Solution

```python
from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda interval: interval[0])
        merged = [intervals[0]]

        for start, end in intervals[1:]:
            last_end = merged[-1][1]

            if start <= last_end:
                merged[-1][1] = max(last_end, end)
            else:
                merged.append([start, end])

        return merged
```
