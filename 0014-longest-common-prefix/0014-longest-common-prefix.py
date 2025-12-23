class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""

        ref =strs[0]
        if ref == "":
            return ""

        for index in range (len(ref)):
            current_char =ref[index]

            for s in strs[1:]:
                if index == len(s) or s[index]!= current_char:
                    return ref[:index]
        return ref
        