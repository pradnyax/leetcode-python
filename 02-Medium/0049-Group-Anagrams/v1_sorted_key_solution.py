# * 4. Group Anagrams
# * Version 1: Sorted Key (Cleanest to Start With)

"""
class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        
        groups = defaultdict(list)

        for word in strs:
            # 1. Create the shared signature ("eat" -> "aet")
            key = "".join(sorted(word))

            # 2. Drop the original word into that signature's bucket -> groups = {"aet": ["eat"]}
            groups[key].append(word)


        # 3. Return just the buckets (values), converted to a list
        return list(groups.values())
"""



# Time complexity : O( m . nlogn )
# Space Complexity : O(m.n)


# NOTE: There is a more optimized approach too! version 2!
