#
# @lc app=leetcode.cn id=485 lang=python3
# @lcpr version=30204
#
# [485] 最大连续 1 的个数
#


# @lcpr-template-start


# @lcpr-template-end
# @lc code=start
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_length = 0
        match_idx = 0
        search_idx = 0
        while search_idx < len(nums):
            while search_idx < len(nums) and nums[search_idx] == 1:
                search_idx += 1
            max_length = max(max_length, search_idx - match_idx)
            search_idx += 1
            match_idx = search_idx
        return max_length


# @lc code=end


#
# @lcpr case=start
# [1,1,0,1,1,1]\n
# @lcpr case=end

# @lcpr case=start
# [1,0,1,1,0,1]\n
# @lcpr case=end

#
