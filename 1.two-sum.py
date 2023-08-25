#
# @lc app=leetcode id=1 lang=python
#
# [1] Two Sum
#

# @lc code=start
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        seen = {}   #to check if we've seen the number before or no

        for i in range(len(nums)):  # looping through the indexes
            if target - nums[i] in seen:  # if when we deduct we find a number already in the dict then thats the answer
                return[seen[target - nums[i]], i] # returning the ans by accessing it using key and the current index
            else:
                seen[nums[i]] = i  # if not seen before just add it
        return[]  #if there is no solution return empty list       

"""I could only solve the brute force version. Looked at the solution to solve this need to solve again."""
# @lc code=en