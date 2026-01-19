class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # store them in hash map with count of each char, then compare
        # Time O(s+t), space length of s+t - for hashmap 
        if len(s) != len(t):
            return False
        countS, countT = {}, {}
        # building the hansmap with count
        for i in range(len(s)):
            countS[s[i]] = 1+ countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)
        for c in countS:
            if countS[c] != countT.get(c,0):
                return False
        return True




        # here everythign is shuffled, we can sort and find, here 
        # Time - O(n log n ) - for sorting, space - s+t, need to optimize run time
        # Quick length check, if length is not same cant be anangram
        # if len(s) != len(t):
        #     return False   
        # Sort both strings - anagrams will have identical sorted versions
        # return sorted(s) == sorted(t)
        