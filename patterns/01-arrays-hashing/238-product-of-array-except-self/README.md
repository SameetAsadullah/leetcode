# Product of Array Except Self

- LeetCode Problem #: 238
- Pattern: Arrays / Hashing
- Link: https://leetcode.com/problems/product-of-array-except-self/

## Problem

Given an integer array `nums`, return an array `answer` such that `answer[i]`
is equal to the product of all the elements of `nums` except `nums[i]`.

The product of any prefix or suffix of `nums` is guaranteed to fit in a 32-bit
integer. The solution must run in `O(n)` time and cannot use division.

## Example

```text
Input: nums = [1, 2, 3, 4]
Output: [24, 12, 8, 6]
```

## Constraints

- `2 <= nums.length <= 10^5`
- `-30 <= nums[i] <= 30`
- The product of any prefix or suffix of `nums` is guaranteed to fit in a
  32-bit integer

## Algorithm

Use the output array to store prefix products, then multiply by postfix
products in a second pass.

1. Initialize `result` with `1`s.
2. Traverse left to right and store the product of all elements before each
   index.
3. Traverse right to left and multiply each index by the product of all
   elements after it.
4. Return the completed result array.

## Why It Works

For each index `i`, the answer is:

```text
product of elements to the left of i
*
product of elements to the right of i
```

The first pass stores the left product for every index. The second pass
multiplies in the right product, so each position ends up with the product of
all elements except itself.

## Complexity

**Time:** `O(n)`

The algorithm makes one pass to build prefix products and one pass to apply
postfix products. Each pass touches every index once, so the total work is
about `2n`, which simplifies to `O(n)`.

**Space:** `O(1)` extra space, excluding the output array

We reuse the output array itself to store intermediate prefix values. Aside
from that required output, only the two running product variables are used.

## Solution

```python
from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = [1] * len(nums)
        prefix = 1

        for i in range(len(nums)):
            result[i] = prefix
            prefix *= nums[i]

        postfix = 1

        for i in range(len(nums) - 1, -1, -1):
            result[i] *= postfix
            postfix *= nums[i]

        return result
```
