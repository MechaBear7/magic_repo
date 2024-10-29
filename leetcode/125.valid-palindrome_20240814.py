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
        n = len(s)

        left, right = 0, n - 1
        while left < right:
            # 从左向右便利找到待匹配字母
            while left < right and not s[left].isalnum():
                left += 1
            # 从右向左找到待匹配字母
            while left < right and not s[right].isalnum():
                right -= 1
            if left < right:
                if s[left].lower() != s[right].lower():
                    return False
            left, right = left + 1, right - 1
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
