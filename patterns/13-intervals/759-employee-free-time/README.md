# Employee Free Time

- LeetCode Problem #: 759
- Pattern: Intervals
- Link: https://leetcode.com/problems/employee-free-time/

## Problem

You are given a list `schedule` of employees, where each employee has a sorted
list of non-overlapping working intervals.

Return the list of finite, positive-length intervals representing the common
free time for all employees.

Note: LeetCode represents each interval as an `Interval` object with `start`
and `end` fields, not as a plain list.

## Example

```text
Input: schedule = [[[1,2],[5,6]],[[1,3]],[[4,10]]]
Output: [[3,4]]
```

## Constraints

- `1 <= schedule.length, schedule[i].length <= 50`
- `0 <= schedule[i][j].start < schedule[i][j].end <= 10^8`
- Each employee's intervals are sorted and non-overlapping

## Algorithm

Flatten all working intervals into one list, sort them, then merge them
implicitly while scanning from left to right.

1. Collect every employee interval into one array.
2. Sort all intervals by start time.
3. Track the end of the current merged busy block in `merged_end`.
4. For each next interval:
5. If its start is greater than `merged_end`, the gap `[merged_end, start]` is
   a common free-time interval.
6. In either case, update `merged_end` to `max(merged_end, interval.end)`.

## Why It Works

Common free time appears exactly in the gaps between merged busy intervals
across all employees.

Once all intervals are flattened and sorted, we do not need to build an
explicit merged list. The variable `merged_end` is enough to represent the end
of the current merged busy block.

If the next interval starts before or at `merged_end`, it overlaps with the
current busy block, so we extend that block by updating `merged_end`. If it
starts after `merged_end`, then the gap between them is a finite interval where
nobody is working, so that gap is common free time.

## Complexity

**Time:** `O(m log m)`

Let `m` be the total number of intervals across all employees. Flattening the
input is `O(m)`, sorting the intervals is `O(m log m)`, and the merge scan is
`O(m)`. The sorting step dominates the total runtime.

**Space:** `O(m)`

We build a flattened list containing all intervals before sorting. The output
list of free intervals is separate from that, so the main extra working space
is linear in the total number of intervals.

## Solution

```python
class Solution:
    def employeeFreeTime(self, schedule):
        intervals = [interval for employee in schedule for interval in employee]
        intervals.sort(key=lambda interval: interval.start)

        free_time = []
        merged_end = intervals[0].end

        for interval in intervals[1:]:
            if interval.start > merged_end:
                free_time.append(Interval(merged_end, interval.start))

            merged_end = max(merged_end, interval.end)

        return free_time
```
