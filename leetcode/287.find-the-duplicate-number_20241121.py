#
# @lc app=leetcode.cn id=287 lang=python3
# @lcpr version=30204
#
# [287] 寻找重复数
#


# @lcpr-template-start


# @lcpr-template-end
# @lc code=start

[1, 2, 2]


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        min_num = 1
        max_num = len(nums) - 1

        while min_num < max_num:
            selected_num = min_num + (max_num - min_num) // 2
            cnts = sum(min_num <= num <= selected_num for num in nums)
            if cnts > selected_num - min_num + 1:
                max_num = selected_num
            else:
                min_num = selected_num + 1

        return min_num


# @lc code=end


#
# @lcpr case=start
# [1,3,4,2,2]\n
# @lcpr case=end

# @lcpr case=start
# [3,1,3,4,2]\n
# @lcpr case=end

# @lcpr case=start
# [3,3,3,3,3]\n
# @lcpr case=end

#
