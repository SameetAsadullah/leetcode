# Valid Palindrome

- LeetCode Problem #: 125
- Pattern: Two Pointers
- Link: https://leetcode.com/problems/valid-palindrome/

## Problem

Given a string `s`, return `true` if it is a palindrome, or `false`
otherwise.

Consider only alphanumeric characters and ignore letter case.

## Example

```text
Input: s = "A man, a plan, a canal: Panama"
Output: true
```

## Constraints

- `1 <= s.length <= 2 * 10^5`
- `s` consists only of printable ASCII characters

## Algorithm

Use two pointers, one starting from the left and one from the right.

1. Move the left pointer until it reaches an alphanumeric character.
2. Move the right pointer until it reaches an alphanumeric character.
3. Compare the lowercase forms of both characters.
4. If they differ, return `false`.
5. If they match, move both pointers inward and continue.

If the pointers cross without a mismatch, the string is a valid palindrome.

## Why It Works

Ignoring punctuation and case means only normalized alphanumeric characters
matter. The two-pointer scan always compares the next valid character from the
left with the next valid character from the right, which is exactly what a
palindrome requires.

## Complexity

- Time: `O(n)`
- Space: `O(1)`

## Solution

```python
class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1

        while left < right:
            while left < right and not s[left].isalnum():
                left += 1

            while left < right and not s[right].isalnum():
                right -= 1

            if s[left].lower() != s[right].lower():
                return False

            left += 1
            right -= 1

        return True
```
