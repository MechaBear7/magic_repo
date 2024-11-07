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
        if len(nums) == 0:
            return 0

        my_set = set()
        for num in nums:
            my_set.add(num)

        num_start = []
        for num in my_set:
            if num - 1 not in my_set:
                num_start.append(num)

        max_len = 1
        for num in num_start:
            length = 0
            cur_num = num
            while cur_num in my_set:
                length += 1
                cur_num += 1
            max_len = max(max_len, length)

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
