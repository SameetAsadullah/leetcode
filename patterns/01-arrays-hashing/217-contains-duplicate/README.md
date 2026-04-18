# Contains Duplicate

- LeetCode Problem #: 217
- Pattern: Arrays / Hashing
- Link: https://leetcode.com/problems/contains-duplicate/

## Problem

Given an integer array `nums`, return `true` if any value appears at least
twice in the array, and return `false` if every element is distinct.

## Example

```text
Input: nums = [1, 2, 3, 1]
Output: true
```

## Constraints

- `1 <= nums.length <= 10^5`
- `-10^9 <= nums[i] <= 10^9`

## Algorithm

Use a set to keep track of numbers already seen.

For each number:
- if it is already in the set, return `true`
- otherwise, add it to the set and continue

If the loop finishes, then all values are distinct, so return `false`.

## Why It Works

A set stores only unique values. The first time a number repeats, checking the
set reveals that the value has already appeared, so we can return immediately.

## Complexity

- Time: `O(n)`
- Space: `O(n)`

## Solution

```python
from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = set()

        for num in nums:
            if num in seen:
                return True
            seen.add(num)

        return False
```
