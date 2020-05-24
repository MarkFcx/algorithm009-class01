#
# @lc app=leetcode.cn id=26 lang=python3
#
# [26] 删除排序数组中的重复项
#

# @lc code=start
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        for i in range(len(nums), 1, -1):
            if (nums[i-1]) == (nums[i-2]):
                nums.pop(i-1)
            else:
                continue
        return len(nums)
# @lc code=end


