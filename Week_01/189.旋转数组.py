#
# @lc app=leetcode.cn id=189 lang=python3
#
# [189] 旋转数组
# 

# @lc code=start
# class Solution(object):
#     def rotate(self, nums, k):
#         """
#         :type nums: List[int]
#         :type k: int
#         :rtype: void Do not return anything, modify nums in-place instead.
#         """
#         n, k, j = len(nums), k % len(nums), 0
#         while n > 0 and k % n != 0:
#             for i in range(0, k):
#                 nums[j + i], nums[len(nums) - k + i] = nums[len(nums) - k + i], nums[j + i] # swap
#             n, j = n - k, j + k
#             k = k % n

# class Solution(object):
#     def rotate(self, nums, k):
#         print("k: ",k)
#         if k is None or k <= 0:
#             return
#         k, end = k % len(nums), len(nums) - 1
#         print(k," ", end)
#         self.reverse(nums, 0, end - k)
#         self.reverse(nums, end - k + 1, end)
#         self.reverse(nums, 0, end)
        
#     def reverse(self, nums, start, end):
#         while start < end:
#             # Python的变量并不直接存储值，而只是引用一个内存地址，交换变量时，只是交换了引用的地址。
#             # 因此这里的空间复杂度就是O(1)
#             nums[start], nums[end] = nums[end], nums[start]
#             start, end = start + 1, end - 1
class Solution(object):
    def rotate(self, nums, k):
            n = len(nums)
            k = k % n
            print("nums[n-k:]:", nums[n-k:])
            nums[:] = nums[n-k:] + nums[:n-k]
# @lc code=end

