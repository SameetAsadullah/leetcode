# Interval List Intersections

- LeetCode Problem #: 986
- Pattern: Intervals
- Link: https://leetcode.com/problems/interval-list-intersections/

## Problem

You are given two lists of closed intervals, `firstList` and `secondList`,
where each list is pairwise disjoint and already sorted.

Return the intersection of these two interval lists.

## Example

```text
Input: firstList = [[0,2],[5,10],[13,23],[24,25]]
       secondList = [[1,5],[8,12],[15,24],[25,26]]
Output: [[1,2],[5,5],[8,10],[15,23],[24,24],[25,25]]
```

## Constraints

- `0 <= firstList.length, secondList.length <= 1000`
- `firstList.length + secondList.length >= 1`
- `0 <= start_i < end_i <= 10^9`
- `end_i < start_{i+1}` in each list

## Algorithm

Use two pointers, one for each list.

1. Compare the current interval from `firstList` with the current interval from
   `secondList`.
2. The overlap starts at the larger start value.
3. The overlap ends at the smaller end value.
4. If the overlap start is less than or equal to the overlap end, add it to the
   answer.
5. Move the pointer whose interval ends first, because that interval cannot
   overlap with any later interval in the other list.

## Why It Works

Since both lists are already sorted and disjoint within themselves, the only
possible intersection at any moment is between the two intervals currently
pointed to by `i` and `j`.

If one interval ends first, it cannot intersect any future interval from the
other list, so it is always safe to move that pointer forward.

## Complexity

**Time:** `O(m + n)`

Each pointer only moves forward, never backward. Across the whole algorithm,
the pointer for `firstList` moves at most `m` times and the pointer for
`secondList` moves at most `n` times, so the total work is linear in the sizes
of the two lists.

**Space:** `O(1)` extra space, excluding the output

Aside from the two indices and a few temporary variables for the overlap
boundaries, no auxiliary data structure is used. The intersections list is the
required output, so it is not counted as extra space here.

## Solution

```python
from typing import List


class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        intersections = []
        i = 0
        j = 0

        while i < len(firstList) and j < len(secondList):
            start = max(firstList[i][0], secondList[j][0])
            end = min(firstList[i][1], secondList[j][1])

            if start <= end:
                intersections.append([start, end])

            if firstList[i][1] < secondList[j][1]:
                i += 1
            else:
                j += 1

        return intersections
```
