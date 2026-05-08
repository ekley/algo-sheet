def is_anagram(s, t):
    if len(s) != len(t):
        return False

    counts = [0] * 26

    for i in range(len(s)):
        counts[ord(s[i]) - ord('a')] += 1
        counts[ord(t[i]) - ord('a')] -= 1

    return all(count == 0 for count in counts)