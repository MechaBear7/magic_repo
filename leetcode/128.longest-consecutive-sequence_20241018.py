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
        my_set = set()
        for num in nums:
            my_set.add(num)

        max_len = 0
        for num in nums:
            if num - 1 not in my_set:
                cur = num
                while cur in my_set:
                    cur += 1
                max_len = max(max_len, cur - num)

        return max_len


# @lc code=end


#
# @lcpr case=start
# [100,4,200,1,3,2]\n
# @lcpr case=end

# @lcpr case=start
# [0,3,7,2,5,8,4,6,0,1]\n
# @lcpr case=end

#
