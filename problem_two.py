# Longest Common Prefix
# def Prefix(text):
#     text.sort()
#
#     first = text[0]
#     last = text[-1]
#     minlength = min(len(first), len(last))
#
#     i = 0
#     while i < minlength and first[i] == last[i]:
#         i += 1
#
#     return first[:i]
#
# text = ['olma', 'olcha', 'olmo']
# print(Prefix(text))


class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        strs.sort()
        firs = strs[0]
        last = strs[-1]
        minlen = min(len(firs), len(last))

        i = 0
        while i < minlen and firs[i] == last[i]:
            i += 1

        return firs[:i]

obj = Solution()
print(obj.longestCommonPrefix(["flower", "flow", "flight"]))

