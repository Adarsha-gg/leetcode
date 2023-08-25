#
# @lc app=leetcode id=242 lang=python
#
# [242] Valid Anagram
#

# @lc code=start
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        first = list(s) # so that it will be easier to iterate
        second = list(t)

        if len(first) == len(second):  # if length not same not anargam ez
            for letters in first:           # check charaacters
                if letters in second:
                    second.remove(letters)   # always remove from the list that you are checking after
                else:                        # cuz if we remove from first set we remove the element
                    return False             # that we've already checked so no point in it.
            return True
        return False        
    

    """Need to do again cuz well brute force onli didn't know the main solution. Easier said than done 🤷‍♂️"""
                
# @lc code=end

