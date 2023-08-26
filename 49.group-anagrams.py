#
# @lc app=leetcode id=49 lang=python
#
# [49] Group Anagrams
#

# @lc code=start
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        final = {}  # empty dict
        
        for words in strs:      #iterate through all words
            all = ''.join(sorted(words))  # the sorted returns single character in a list so combine it into 1
            if all not in final: # check if in the dict if not create a empty list
                final[all] = []
            final[all].append(words)  #append every single WORD not sorted string

        return list(final.values())    #return in list form


# @lc code=end

