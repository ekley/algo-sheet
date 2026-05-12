# problem explained at 3:32:00
# problem: Longest Repeating Character Replacement

def character_replacement(s, k):
    count = {}
    left = 0
    max_freq = 0
    result = 0

    for right in range(len(s)):
        char = s[right]

        count[char] = count.get(char, 0) + 1
        max_freq = max(max_freq, count[char])

        # If window is invalid, shrink it
        while (right - left + 1) - max_freq > k:
            count[s[left]] -= 1
            left += 1

        result = max(result, right - left + 1)

    return result


# Example
s = "ABABBA"
k = 2

print(character_replacement(s, k))