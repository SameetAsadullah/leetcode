# Group Anagrams

- LeetCode Problem #: 49
- Pattern: Arrays / Hashing
- Link: https://leetcode.com/problems/group-anagrams/

## Problem

Given an array of strings `strs`, group the anagrams together.

An anagram is a word formed by rearranging the letters of another word. Words
that have the same character frequencies belong in the same group.

## Example

```text
Input: strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
Output: [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]
```

The order of the groups and the order of strings inside each group can vary.

## Constraints

- `1 <= strs.length <= 10^4`
- `0 <= strs[i].length <= 100`
- `strs[i]` consists of lowercase English letters

## Algorithm

Use a hash map where the key represents the character frequency of a word.

For each word:
- create an array of `26` zeroes
- count how many times each lowercase letter appears
- convert the count array into a tuple so it can be used as a hash map key
- append the word to the group for that key

At the end, return all grouped values from the hash map.

## Why It Works

Anagrams have exactly the same character frequencies. For example, `"eat"`,
`"tea"`, and `"ate"` all produce the same count key, so they are placed in the
same group.

## Complexity

Let `n` be the number of strings and `k` be the maximum string length.

**Time:** `O(n * k)`

There are `n` strings, and for each string we may scan all `k` of its
characters to build the 26-count signature. The tuple conversion is constant
size because the array always has length 26, so the per-word cost is still
dominated by scanning the characters.

**Space:** `O(n * k)`

The grouped output stores all original strings, so the total stored content is
proportional to the total input size. The hash map also needs one key per
anagram group, but that does not exceed the same overall scale.

## Solution

```python
from collections import defaultdict
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)
        offset = ord("a")

        for word in strs:
            counts = [0] * 26

            for char in word:
                counts[ord(char) - offset] += 1

            groups[tuple(counts)].append(word)

        return list(groups.values())
```
