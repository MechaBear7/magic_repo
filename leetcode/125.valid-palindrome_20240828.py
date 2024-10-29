#
# @lc app=leetcode.cn id=125 lang=python3
# @lcpr version=30204
#
# [125] 验证回文串
#


# @lcpr-template-start


# @lcpr-template-end
# @lc code=start
class Solution:
    def isPalindrome(self, s: str) -> bool:
        left_idx = 0
        right_idx = len(s) - 1
        while left_idx < right_idx:
            while left_idx < right_idx and not s[left_idx].isalnum():
                left_idx += 1
            while left_idx < right_idx and not s[right_idx].isalnum():
                right_idx -= 1
            if left_idx < right_idx and s[left_idx].lower() != s[right_idx].lower():
                return False
            left_idx, right_idx = left_idx + 1, right_idx - 1
        return True


# @lc code=end


#
# @lcpr case=start
# "A man, a plan, a canal: Panama"\n
# @lcpr case=end

# @lcpr case=start
# "race a car"\n
# @lcpr case=end

# @lcpr case=start
# " "\n
# @lcpr case=end

#
