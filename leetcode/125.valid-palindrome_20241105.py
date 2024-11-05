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
        left, right = 0, len(s) - 1
        while left < right:
            while left < right and not s[left].lower().isalnum():
                left += 1
            while right > left and not s[right].lower().isalnum():
                right -= 1
            if s[left].lower() == s[right].lower():
                left, right = left + 1, right - 1
            else:
                return False

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
