class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        dict = {}

        for i in range(len(s)):
            if s[i] in dict:
                if dict[s[i]] != t[i]:
                    return False
            else:
                if t[i] in dict.values():  
                    return False
                dict[s[i]] = t[i]
        return True




# {}
#// e
#//if e is in Dict 
#Existoing dict value for e is chceking with T value 
#dict pair of e =! a - false
#if not in dict :
 #   key is not there but vlue is here : hence diffrent cgar us mapped here
  #  false
   # Then add the value 

