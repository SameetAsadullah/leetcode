# Valid Anagram

- LeetCode Problem #: 242
- Pattern: Arrays / Hashing
- Link: https://leetcode.com/problems/valid-anagram/

## Problem

Given two strings `s` and `t`, return `true` if `t` is an anagram of `s`,
and return `false` otherwise.

An anagram uses the same characters with the same frequencies, only in a
different order.

## Example

```text
Input: s = "anagram", t = "nagaram"
Output: true
```

## Constraints

- `1 <= s.length, t.length <= 5 * 10^4`
- `s` and `t` consist of lowercase English letters

## Approach 1: Hash Map

Use a hash map to count character frequencies.

1. If the string lengths are different, return `false`.
2. Count each character in `s`.
3. Traverse `t` and subtract from the counts.
4. If a character is missing or its count goes below zero, return `false`.
5. If the loop finishes, the strings are anagrams.

### Why It Works

Two strings are anagrams only if every character appears the same number of
times in both strings. The frequency map stores that requirement directly.

### Complexity

- Time: `O(n)`
- Space: `O(n)`

### Solution

```python
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        counts = {}

        for char in s:
            counts[char] = counts.get(char, 0) + 1

        for char in t:
            if char not in counts:
                return False

            counts[char] -= 1

            if counts[char] < 0:
                return False

        return True
```

## Approach 2: Frequency Array

If the input is limited to lowercase English letters, a fixed array of length
`26` is more efficient than a hash map.

1. If the lengths are different, return `false`.
2. Create an array of `26` zeroes.
3. For each index, increment the count for `s[i]` and decrement the count for
   `t[i]`.
4. If every final count is `0`, the strings are anagrams.

### Why It Works

Each position in the array represents one lowercase letter from `a` to `z`.
Matching characters cancel each other out, so every count must end at `0`.

### Complexity

- Time: `O(n)`
- Space: `O(1)`

### Solution

```python
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        counts = [0] * 26
        offset = ord("a")

        for i in range(len(s)):
            counts[ord(s[i]) - offset] += 1
            counts[ord(t[i]) - offset] -= 1

        for count in counts:
            if count != 0:
                return False

        return True
```

## Which One To Use

- Use the hash map solution when you want the more general approach.
- Use the frequency array when the problem guarantees lowercase English letters.
