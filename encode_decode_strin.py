class Solution:

    def encode(self, strs):
        encoded = ""
        for s in strs:
            encoded += str(len(s)) + "#" + s
        return encoded

    def decode(self, s):
        res = []
        i = 0

        while i < len(s):
            j = i

            # find the '#'
            while s[j] != "#":
                j += 1

            length = int(s[i:j])
            j += 1  # skip '#'

            word = s[j:j + length]
            res.append(word)

            i = j + length

        return res


sol = Solution()
encoded_str = sol.encode(["leet", "code"])
print(sol.decode(encoded_str))