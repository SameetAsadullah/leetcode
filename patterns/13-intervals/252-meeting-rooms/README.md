# Meeting Rooms

- LeetCode Problem #: 252
- Pattern: Intervals
- Link: https://leetcode.com/problems/meeting-rooms/

## Problem

Given an array of meeting time intervals where `intervals[i] = [start_i, end_i]`,
determine if a person could attend all meetings.

## Example

```text
Input: intervals = [[0,30],[5,10],[15,20]]
Output: false
```

## Constraints

- `0 <= intervals.length <= 10^4`
- `intervals[i].length == 2`
- `0 <= start_i < end_i <= 10^6`

## Algorithm

Sort the meetings by start time, then check neighboring intervals for overlap.

1. Sort intervals by their start value.
2. Traverse from left to right.
3. Compare each meeting with the one immediately before it.
4. If the current start time is smaller than the previous end time, the
   meetings overlap and the person cannot attend all of them.

## Why It Works

After sorting by start time, any overlap that matters must happen between two
adjacent intervals in that sorted order.

If `intervals[i]` starts before `intervals[i - 1]` ends, then those two
meetings overlap. If no adjacent pair overlaps, then the whole schedule is
non-overlapping, so attending every meeting is possible.

## Complexity

**Time:** `O(n log n)`

Sorting the intervals by start time takes `O(n log n)`. After sorting, we only
make one linear pass through the list to check neighboring meetings, so the
sorting step dominates the total runtime.

**Space:** `O(1)` extra space, excluding Python's sort internals

The overlap check itself only uses the loop index and direct comparisons. No
additional data structure is needed after sorting.

## Solution

```python
from typing import List


class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        intervals.sort(key=lambda interval: interval[0])

        for i in range(1, len(intervals)):
            if intervals[i][0] < intervals[i - 1][1]:
                return False

        return True
```
