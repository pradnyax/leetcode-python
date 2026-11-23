# * Approach 2: Character Count Tuple as the Key
# * Optimal solution

"""
class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:

        groups = defaultdict(list)

        for word in strs:
            count = [0] * 26  # 26 zeros for a-z
            for char in word:
                count[ord(char) - ord("a")] += 1

            # Convert list to tuple so it can be a dict key
            groups[tuple(count)].append(word)

        return list(groups.values())
"""

# NOTE:
# ! Time: O(m.n) --> no sorting, just one pass over every letter of every word.
# ! Space: O(m.n)
