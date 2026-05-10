# Container With Most Water

- LeetCode Problem #: 11
- Pattern: Two Pointers
- Link: https://leetcode.com/problems/container-with-most-water/

## Problem

You are given an integer array `height` of length `n`.

There are `n` vertical lines drawn such that the two endpoints of the `i`th
line are `(i, 0)` and `(i, height[i])`.

Find two lines that, together with the x-axis, form a container that holds the
most water.

Return the maximum amount of water a container can store.

## Example

```text
Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
```

## Constraints

- `n == height.length`
- `2 <= n <= 10^5`
- `0 <= height[i] <= 10^4`

## Algorithm

Use two pointers, one at each end of the array.

1. Compute the water area formed by the two lines.
2. Update the best answer seen so far.
3. Move the pointer with the smaller height inward.

The reason for step 3 is that the width always decreases, so the only hope of
finding a larger area is to try a taller line.

## Why It Works

The area is determined by:

```text
width * min(left_height, right_height)
```

If one side is shorter, that shorter side limits the area. Moving the taller
side cannot help, because the width becomes smaller and the limiting height
does not improve. So the correct move is always to shift the shorter side.

## Complexity

**Time:** `O(n)`

Each step moves exactly one pointer inward. Since `left` can move right at most
`n - 1` times and `right` can move left at most `n - 1` times, the loop
performs only a linear number of iterations.

**Space:** `O(1)`

The algorithm stores only the two pointers, the current area information, and
the best answer found so far.

## Solution

```python
from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        best = 0

        while left < right:
            width = right - left
            current_height = min(height[left], height[right])
            best = max(best, width * current_height)

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return best
```
