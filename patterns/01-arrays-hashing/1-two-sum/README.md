# Two Sum

- LeetCode Problem #: 1
- Pattern: Arrays / Hashing
- Link: https://leetcode.com/problems/two-sum/

## Problem

Given an array of integers `nums` and an integer `target`, return the indices
of the two numbers such that they add up to `target`.

You may assume that each input has exactly one solution, and you may not use
the same element twice.

## Example

```text
Input: nums = [2, 7, 11, 15], target = 9
Output: [0, 1]
```

## Constraints

- `2 <= nums.length <= 10^4`
- `-10^9 <= nums[i] <= 10^9`
- `-10^9 <= target <= 10^9`
- Only one valid answer exists

## Algorithm

Use a hash map to store numbers already seen and their indices.

For each number:
- compute the complement as `target - num`
- check whether the complement is already in the hash map
- if it is, return the stored index and the current index
- otherwise, store the current number and continue

## Why It Works

If the correct pair exists, then when the second number is reached, the first
number has already been stored in the hash map. That lets us find the answer
in constant time for each element.

## Complexity

**Time:** `O(n)`

We make one left-to-right pass through `nums`. For each element, we do a
constant amount of work: compute the complement, check the hash map, and
possibly insert the current value. Since hash map lookup and insert are `O(1)`
on average, the full pass stays linear.

**Space:** `O(n)`

In the worst case, the answer is found near the end, so the hash map may need
to store almost every earlier number and its index.

## Solution

```python
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}

        for index, num in enumerate(nums):
            complement = target - num
            if complement in seen:
                return [seen[complement], index]
            seen[num] = index

        return []
```
