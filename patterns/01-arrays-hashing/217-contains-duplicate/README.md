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

## Approach 1: Set Scan

Use a set to keep track of numbers already seen.

For each number:
- if it is already in the set, return `true`
- otherwise, add it to the set and continue

If the loop finishes, then all values are distinct, so return `false`.

### Why It Works

A set stores only unique values. The first time a number repeats, checking the
set reveals that the value has already appeared, so we can return immediately.

### Complexity

**Time:** `O(n)`

We examine each value once. For every value, we only do a membership check and
possibly an insert into the set, both of which are `O(1)` on average. That
keeps the whole scan linear.

**Space:** `O(n)`

If there are no duplicates, the set grows to contain every element from the
input.

### Solution

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

## Approach 2: One-Liner With `set`

Convert the array to a set and compare lengths.

If duplicates exist, the set becomes smaller because it stores only unique
values.

### Why It Works

`set(nums)` removes duplicate values. If its length is smaller than the
original array length, then at least one duplicate exists.

### Complexity

**Time:** `O(n)`

Converting `nums` into a set requires reading all elements once. After that,
the length comparison is constant time.

**Space:** `O(n)`

The constructed set may contain all input values when they are all distinct.

### Solution

```python
from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(set(nums)) != len(nums)
```

## Which One To Use

- Use the set scan if you want the logic to be more explicit.
- Use the one-liner if you want the shortest clean Python solution.
