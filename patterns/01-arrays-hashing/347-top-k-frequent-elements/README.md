# Top K Frequent Elements

- LeetCode Problem #: 347
- Pattern: Arrays / Hashing
- Link: https://leetcode.com/problems/top-k-frequent-elements/

## Problem

Given an integer array `nums` and an integer `k`, return the `k` most frequent
elements.

You may return the answer in any order.

## Example

```text
Input: nums = [1, 1, 1, 2, 2, 3], k = 2
Output: [1, 2]
```

## Constraints

- `1 <= nums.length <= 10^5`
- `-10^4 <= nums[i] <= 10^4`
- `1 <= k <=` number of unique elements in `nums`
- The answer is guaranteed to be unique

## Algorithm

Use a hash map to count frequencies, then use bucket sort to collect numbers by
frequency.

1. Count how many times each number appears.
2. Create `len(nums) + 1` buckets, where index `i` stores numbers that appear
   exactly `i` times.
3. Put each number into the bucket matching its frequency.
4. Iterate from the highest frequency bucket down to the lowest.
5. Collect numbers until `k` elements have been added.

## Why It Works

Numbers with the same frequency go into the same bucket. Traversing the buckets
from highest frequency to lowest guarantees that the first `k` numbers gathered
are the `k` most frequent elements.

## Complexity

**Time:** `O(n)`

The work happens in three phases. First, we count each value once in `O(n)`.
Second, we place each distinct value into one frequency bucket, which is at
most another `O(n)` total. Third, we scan the bucket array from back to front.
Even though there is a nested loop, each number is appended to the result at
most once, so the total bucket scan is still linear overall.

**Space:** `O(n)`

The frequency map may store every distinct number. The bucket array has
`len(nums) + 1` slots, and the final answer can contain up to `k` numbers.
Altogether, the extra storage grows linearly with the input size.

## Solution

```python
from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}
        buckets = [[] for _ in range(len(nums) + 1)]
        result = []

        for num in nums:
            counts[num] = counts.get(num, 0) + 1

        for num, frequency in counts.items():
            buckets[frequency].append(num)

        for frequency in range(len(buckets) - 1, 0, -1):
            for num in buckets[frequency]:
                result.append(num)
                if len(result) == k:
                    return result

        return result
```
