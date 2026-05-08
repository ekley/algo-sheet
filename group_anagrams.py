def group_anagrams(strs):
    result = {}

    for word in strs:
        count = [0] * 26

        for ch in word:
            count[ord(ch) - ord('a')] += 1

        key = tuple(count)

        if key not in result:
            result[key] = []
        result[key].append(word)

    return list(result.values())