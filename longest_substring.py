# problem explained at 3:32:00
# problem: longest sunbstring without repeating characters

def length_of_longest_substring(s):
    seen = set()

    left = 0
    max_length = 0

    for right in range(len(s)):

        while s[right] in seen:
            seen.remove(s[left])
            left += 1

        seen.add(s[right])

        max_length = max(max_length, right - left + 1)

    return max_length


# Example
# we put two pointers, left and right vars, then we stretch the right pointer to the right, 
# as we progress we need to omit one character(which is seen) from the substring whiche means moving left pointer to the right.
#    l r
s = "abcabcbb"

print(length_of_longest_substring(s)) # 3