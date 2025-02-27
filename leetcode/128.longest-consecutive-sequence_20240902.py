#
# @lc app=leetcode.cn id=128 lang=python3
# @lcpr version=30204
#
# [128] 最长连续序列
#


# @lcpr-template-start


# @lcpr-template-end
# @lc code=start
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        max_length = 0
        myset = set(nums)
        for num in nums:
            if num - 1 not in myset:
                length = 0
                cur_num = num
                while cur_num in myset:
                    length += 1
                    cur_num += 1
                max_length = max(max_length, length)
        return max_length


# @lc code=end


#
# @lcpr case=start
# [100,4,200,1,3,2]\n
# @lcpr case=end

# @lcpr case=start
# [0,3,7,2,5,8,4,6,0,1]\n
# @lcpr case=end

#
