#
# @lc app=leetcode id=217 lang=python
#
# [217] Contains Duplicate
#

# @lc code=start
class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        
        seen = {}

        for num in nums: 
            if num in seen: # if its added to dict then just check if not add 
                return True
            else:
                seen[num] = 0
        return False        
# @lc code=end

