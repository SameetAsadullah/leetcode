# Meeting Rooms II

- LeetCode Problem #: 253
- Pattern: Intervals
- Link: https://leetcode.com/problems/meeting-rooms-ii/

## Problem

Given an array of meeting time intervals where `intervals[i] = [start_i, end_i]`,
return the minimum number of conference rooms required.

## Example

```text
Input: intervals = [[0,30],[5,10],[15,20]]
Output: 2
```

## Constraints

- `0 <= intervals.length <= 10^4`
- `intervals[i].length == 2`
- `0 <= start_i < end_i <= 10^6`

## Algorithm

Sort the meetings by start time and use a min-heap to track the current room
end times.

1. Sort intervals by start time.
2. Put the end time of the first meeting into a min-heap.
3. For each next meeting:
4. If its start time is at least the smallest end time in the heap, reuse that
   room by popping the heap.
5. Push the current meeting's end time into the heap.
6. At the end, the heap size is the number of rooms needed.

## Why It Works

The min-heap always stores the end times of meetings that are currently using
rooms. The smallest end time is the room that becomes available first.

If the next meeting starts after or exactly when that earliest meeting ends, we
can reuse the same room. Otherwise, every existing room is still occupied, so a
new room is required. Because the heap tracks all active meetings, its size at
any moment is exactly the number of rooms in use.

## Complexity

**Time:** `O(n log n)`

Sorting the meetings by start time costs `O(n log n)`. Then we process each
meeting once, and each heap push or pop costs `O(log n)`. Since there can be up
to one push and one pop per meeting, the total heap work is also `O(n log n)`.

**Space:** `O(n)`

In the worst case, all meetings overlap, so the heap must store the end time of
every meeting at the same time.

## Solution

```python
import heapq
from typing import List


class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0

        intervals.sort(key=lambda interval: interval[0])
        min_heap = [intervals[0][1]]

        for start, end in intervals[1:]:
            if start >= min_heap[0]:
                heapq.heappop(min_heap)

            heapq.heappush(min_heap, end)

        return len(min_heap)
```
