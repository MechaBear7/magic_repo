#
# @lc app=leetcode.cn id=9 lang=python3
# @lcpr version=30204
#
# [9] 回文数
#


# @lcpr-template-start


# @lcpr-template-end
# @lc code=start
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        nums = []
        while x > 0:
            nums.append(x % 10)
            x = x // 10
        left, right = 0, len(nums) - 1
        while left < right:
            if nums[left] != nums[right]:
                return False
            left, right = left + 1, right - 1
        return True


# @lc code=end


#
# @lcpr case=start
# 121\n
# @lcpr case=end

# @lcpr case=start
# -121\n
# @lcpr case=end

# @lcpr case=start
# 10\n
# @lcpr case=end

#
