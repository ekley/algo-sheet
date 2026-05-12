# problem: explained at 3:11:00
# problem: find if any permutation of s1 string exists as substring in s2

def check_inclusion(s1: str, s2: str) -> bool:
    if len(s1) > len(s2):
        return False

    s1Count = [0] * 26
    s2Count = [0] * 26

    for i in range(len(s1)):
        s1Count[ord(s1[i]) - ord('a')] += 1
        s2Count[ord(s2[i]) - ord('a')] += 1

    matches = 0

    for i in range(26):
        if s1Count[i] == s2Count[i]:
            matches += 1

    l = 0

    for r in range(len(s1), len(s2)):
        if matches == 26:
            return True

        index = ord(s2[r]) - ord('a')
        s2Count[index] += 1

        if s1Count[index] == s2Count[index]:
            matches += 1 # we gained a match
        elif s1Count[index] + 1 == s2Count[index]: # before adding they were equall
            matches -= 1 # we lost a match

        index = ord(s2[l]) - ord('a')
        s2Count[index] -= 1

        if s1Count[index] == s2Count[index]:
            matches += 1 # we gained a match
        elif s1Count[index] - 1 == s2Count[index]: # before removing they were equall
            matches -= 1 # we lost a match

        l += 1

    return matches == 26


s1 = "ab"
s2 = "eidbaooo"

print(check_inclusion(s1, s2))

# ------------------------------------------------
# Example
# ------------------------------------------------

s1 = "ab"
s2 = "eidbaooo"

print(check_inclusion(s1, s2))