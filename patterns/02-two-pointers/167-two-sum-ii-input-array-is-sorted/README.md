# Two Sum II - Input Array Is Sorted

- LeetCode Problem #: 167
- Pattern: Two Pointers
- Link: https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/

## Problem

Given a 1-indexed array of integers `numbers` that is sorted in
non-decreasing order, find two numbers such that they add up to a specific
target.

Return the indices of the two numbers as `[index1, index2]`, where
`1 <= index1 < index2 <= numbers.length`.

The tests are generated such that there is exactly one solution, and the same
element may not be used twice.

## Example

```text
Input: numbers = [2, 7, 11, 15], target = 9
Output: [1, 2]
```

## Constraints

- `2 <= numbers.length <= 3 * 10^4`
- `-1000 <= numbers[i] <= 1000`
- `numbers` is sorted in non-decreasing order
- `-1000 <= target <= 1000`
- Exactly one valid solution exists

## Algorithm

Use two pointers because the array is already sorted.

1. Start `left` at the beginning and `right` at the end.
2. Compute the sum of `numbers[left] + numbers[right]`.
3. If the sum is too small, move `left` rightward to increase it.
4. If the sum is too large, move `right` leftward to decrease it.
5. If the sum matches the target, return the 1-indexed positions.

## Why It Works

Since the array is sorted:
- moving `left` to the right makes the sum larger
- moving `right` to the left makes the sum smaller

That means each pointer move gets us closer to the target without missing the
correct pair.

## Complexity

**Time:** `O(n)`

On every iteration, exactly one pointer moves inward. Because neither pointer
ever moves backward, the two pointers can cross after at most one full pass
across the array.

**Space:** `O(1)`

No auxiliary structure is needed because the sorted order itself gives the
information we need to adjust the sum.

## Solution

```python
from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1

        while left < right:
            current_sum = numbers[left] + numbers[right]

            if current_sum == target:
                return [left + 1, right + 1]

            if current_sum < target:
                left += 1
            else:
                right -= 1

        return []
```
