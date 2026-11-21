"""
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        # 1. Edge case: diff length can't be anagrams
        if len(s) != len(t):
            return False

        count_s = {}
        count_t = {}

        # 2. Count frequencies in both strings at the same time
        for i in range(len(s)):
            count_s[s[i]] = count_s.get(s[i], 0) + 1
            count_t[t[i]] = count_t.get(t[i],0) + 1

        # 3. Compare the two frequency maps
        return count_s == count_t


        # -----------------------------------------------------
        # ===my old approach===

        # return sorted(s) == sorted(t)
        # return Counter(s) == Counter(t)
        # if len(s) != len(t):
        #     return False
        # count_s, count_t = {},{}
        # for i in range(len(s)):
        #     count_s[s[i]] = count_s.get(s[i],0) + 1
        #     count_t[t[i]] = count_t.get(t[i],0) + 1
        # return count_s == count_t
"""
